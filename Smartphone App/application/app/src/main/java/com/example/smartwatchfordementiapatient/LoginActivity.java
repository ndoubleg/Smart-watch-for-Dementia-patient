package com.example.smartwatchfordementiapatient;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

public class LoginActivity extends AppCompatActivity {

    private EditText username_et;
    private EditText password_et;
    private Button login_btn;
    private Button signin_btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        username_et=findViewById(R.id.login_id_et);
        password_et=findViewById(R.id.login_pw_et);
        login_btn=findViewById(R.id.login_bt);

        //click the login button
        login_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                //connet to server to get login data...

                //then move to next page
                //move to next page

                Toast.makeText(getApplicationContext(), "success log in", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(getApplicationContext(), LocationRegisterActivity.class);
                startActivity(intent);
                finish();

            }
        });

    }
}