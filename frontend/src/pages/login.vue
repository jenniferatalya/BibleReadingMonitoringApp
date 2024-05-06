<template>
<v-app>
    <v-container class="login">
      <v-card tile elevation="1">
        <v-card-title>
          <h1>Login</h1>
        </v-card-title> 
        
        <v-form v-model="isvalid">
          <v-card-text>
            <v-text-field :rules="usernameRules" label="Username" v-model="user.username"/>  
            <v-text-field :rules="passwordRules" label="Password"
            :type="showPassword ? 'text' : 'password' " 
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off' " 
            @click:append="handleclick" v-model="user.password"/>
          </v-card-text>
          
          <v-divider></v-divider>
          <v-card-actions> 
            <v-btn color="success" @click="handlesubmit" :disabled="!isvalid">Login</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-container>  
  </v-app>
  </template>
  
  <script>
  export default {
    name: 'Login',
    data () {
      return {
        showPassword: false,
        user: {
          username: '',
          password: ''
        },
        usernameRules: [
          value => value != '' || 'Username is required'
        ],
        passwordRules: [
          value => value != '' || 'Password is required'
        ],
        isvalid: false
      }
    },  
    methods: {
      handleclick () {
        this.showPassword =!this.showPassword
      },
      handlesubmit() {
        console.log(this.user)
        if (this.user.username == 'rennifer' && this.user.password == 'lulus') {
          this.$router.push('/dashboard');
        } else {
          alert('Incorrect username or password!');
        }
        this.user.username = '';
        this.user.password = '';
        }
      }
    };
  </script>