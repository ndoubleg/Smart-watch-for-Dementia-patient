package com.example.smartwatchfordementiapatient;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import android.content.Intent;
import android.location.Address;
import android.location.Geocoder;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.material.navigation.NavigationView;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity implements OnMapReadyCallback {

    private TextView current_address_tv;

    private GoogleMap mMap;

    private NavigationView navigationView;
    private DrawerLayout drawer_layout;
    private ImageButton menu_btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //google map initial setting
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        //if get patient's location(latitude, longitude) from server, change to address by using 'getCurrentAddress' function
        current_address_tv=findViewById(R.id.current_address_tv);


        drawer_layout=findViewById(R.id.drawer_layout);
        navigationView=findViewById(R.id.navigation_menu);

        //click menu button
        menu_btn=findViewById(R.id.menu_btn);
        menu_btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                drawer_layout.openDrawer(GravityCompat.START);
            }
        });

        //navigation menu
        navigationView=findViewById(R.id.navigation_menu);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(MenuItem menuItem) {
                menuItem.setChecked(true);
                drawer_layout.closeDrawers();

                int id = menuItem.getItemId();
                String title = menuItem.getTitle().toString();

                if(id == R.id.menu_location_setting){
                    startActivity(new Intent(getApplicationContext(),LocationSettingActivity.class));
                }
                else if(id == R.id.menu_mypage){
                    startActivity(new Intent(getApplicationContext(),MyPageActivity.class));

                }
                return true;
            }
        });

    }



    //google map setting
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        //latitude, longitude should be changed to patient's current location
        //location should be get from server db

        LatLng seoul = new LatLng(40.42317701770357, -86.92853180767158);
        mMap.addMarker(new MarkerOptions().position(seoul).title("seoul"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(seoul));
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(seoul,14));

        current_address_tv.setText(getCurrentAddress(40.42317701770357, -86.92853180767158));

    }

    //geocoder : longtitude, latitude <-> address
    public String getCurrentAddress( double latitude, double longitude) {

        //지오코더
        // GPS를 주소로 변환
        Geocoder geocoder = new Geocoder(this, Locale.getDefault());

        List<Address> addresses;

        try {
            addresses = geocoder.getFromLocation(latitude, longitude, 7);
        } catch (IOException ioException) {
            //네트워크 문제w
            return "geocorder not service";
        } catch (IllegalArgumentException illegalArgumentException) {
            //Toast.makeText(this, "잘못된 GPS 좌표", Toast.LENGTH_LONG).show();
            return "wrong gps location";
        }
        if (addresses == null || addresses.size() == 0) {
            //Toast.makeText(this, "주소 미발견", Toast.LENGTH_LONG).show();
            return "couldn't search address";
        }

        Address address = addresses.get(0);
        String addr=address.getAddressLine(0);
//        addr=addr.substring(4);
        //return address.getAddressLine(0).toString()+"\n";
        return addr;
    }


}