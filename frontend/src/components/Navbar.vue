<template>
    <v-app>
        <v-navigation-drawer v-model="sidebar" app>
        <v-list>
          <v-list-tile v-for="item in menuItem" :key="item.title" :to="item.path">
            <v-list-tile-content>{{ item.title }}</v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>
  
      <v-toolbar app>
        <span class="hidden-sm-and-up">
          <v-toolbar-side-icon @click="sidebar = !sidebar"> </v-toolbar-side-icon>
        </span>
        <v-toolbar-title>
          <router-link to="/" tag="span" style="cursor: pointer">
            {{ appTitle }}
          </router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-xs-only">
          <v-btn flat v-for="item in menuItems" :key="item.title" :to="item.path">
            <v-icon left dark>{{ item.icon }}</v-icon>
            {{ item.title }}
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
  
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>
</template>
  
  <script>
  export default {
    name: "App",
    data() {
      return {
        sidebar: false,
        menuItems: [
          { title: "Dashboard", path: "/dashboard" },
          { title: "Report", path: "/report" },
          { title: "Group", path: "/group" },
          { title: "User", path: "/user" },
          { title: "Admin", path: "/admin" },
          { title: "Church", path: "/church" },
          { title: "Signout", path: "/login" },
        ],
      };
    },
  };
  </script>