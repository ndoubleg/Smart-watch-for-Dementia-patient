package com.example.smartwatchfordementiapatient;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;


public class LocationSettingActivity extends AppCompatActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private Button complete_btn;
    private Button cancel_btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location_setting);


        //click complete button
        complete_btn=findViewById(R.id.complete_btn);
        complete_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                //connet to server to send location data..

                //then move to next page
                //move to next page
                Toast.makeText(getApplicationContext(), "complete modify location", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(intent);
                finish();

            }
        });

        cancel_btn=findViewById(R.id.cancel_btn);
        cancel_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "cancel location setting", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(intent);
                finish();
            }
        });

        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // touch on map -> change mark point
        mMap.setOnMapClickListener(new GoogleMap.OnMapClickListener(){
            @Override
            public void onMapClick(LatLng point) {
                MarkerOptions mOptions = new MarkerOptions();
                // marker title
                mOptions.title("");
                mMap.clear();

                Double latitude = point.latitude; // 위도
                Double longitude = point.longitude; // 경도
                // 마커의 스니펫(간단한 텍스트) 설정
                mOptions.snippet(latitude + ", " + longitude);
                // LatLng: 위도 경도 쌍을 나타냄
                mOptions.position(new LatLng(latitude, longitude));

                // 반경 1KM원
                CircleOptions circle1KM = new CircleOptions().center(new LatLng(latitude, longitude)) //latitude & longitude of point
                        .radius(1000)      //radius unit : m
                        .strokeWidth(0f)  //line width -> 0f = no line
                        .fillColor(Color.parseColor("#885b9fde")); //background color

                // add marker & circle
                googleMap.addMarker(mOptions);
                googleMap.addCircle(circle1KM);

            }
        });

        //latitude, longitude should be changed to current location
        LatLng seoul = new LatLng(37.56638872588792, 126.97800947033107);
        mMap.addMarker(new MarkerOptions().position(seoul).title("seoul"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(seoul));
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(seoul,14));

        // 반경 1KM원
        CircleOptions circle1KM = new CircleOptions().center(seoul) //latitude & longitude of point
                .radius(1000)      //radius unit : m
                .strokeWidth(0f)  //line width -> 0f = no line
                .fillColor(Color.parseColor("#885b9fde")); //background color

        mMap.addCircle(circle1KM);

    }

}