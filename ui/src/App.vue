<template>
  <v-app>
    <div class="wema">
      <v-card class="home">
        <div class="logo rounded-circle">
          <img  src="./assets/wemaLogo.png"/>
        </div>
        <div class="nav">
          <v-tabs v-model="tab">
            <v-tab to="/">Welcome</v-tab>
            <v-tab to="/about">About</v-tab>
            <v-tab to="/calendar">Calendar</v-tab>
            <v-tab>Tuition</v-tab>
          </v-tabs>
        </div>
        <v-main>
          <router-view></router-view>
        </v-main>
      </v-card>
    </div>
      
    
  </v-app>
</template>

<script>

export default {
  name: "App",
  data: () => ({
    return: {
      tab: 0
    }
  }),
};
</script>
<style lang="scss">

$font-family:'Optima';

.v-application {
  [class*='text-'] {
    color: #36405a;
    font-family: $font-family, sans-serif !important;
  }
  font-family: $font-family, sans-serif !important;
}
body{
  background-color: #d1e3e9;
}
.v-main{
  z-index: 9999
}
.wema{
  height: 100vh;
  width: 100vw;
  padding: 1rem;
  display: flex;
  justify-content: center;
  .v-card.home{
    margin-top: 6rem;
    margin-bottom: 6rem;
    width: 1250px;
    position: relative;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    background-color: #2a3950;
    box-shadow: 3px -3px 6px rgba(255, 255, 255, 0.5), 
      1px -1px 2px rgba(204, 198, 198, 0.616), 
      inset -2px 2px 10px rgba(255, 255, 255, 0.4), 
      inset 2px -2px 7px rgb(139 161 169 / 77%), 
      -3px 3px 20px rgb(139 161 169 / 77%), 
      -1px 1px 2px rgb(139 161 169 / 77%) !important;
    .logo{
      position: absolute;
      z-index: 999;
      left: 0;
      top: -7rem;
      margin: 1rem;
      width: 200px;
      height: 200px;
      opacity: .95;
      box-shadow: 3px -3px 6px rgba(255, 255, 255, 0.5), 
        1px -1px 2px rgba(255, 255, 255, 0.616), 
        inset -2px 2px 10px rgba(255, 255, 255, 0.212), 
        -3px 3px 6px rgba(0, 0, 0, 0.3), 
        -1px 1px 2px rgba(0, 0, 0, 0.5);
      
      img{
        width: 100%;
        height: 100%;
      }
    }
    .nav{
      padding: .5rem 3rem;
      overflow: hidden;
      position: absolute;
      top: -4rem;
      left: 200px; 
      width: calc(100% - 2rem);
      border-radius: 5px;
      .v-tabs{
        .v-tabs-bar{
          background-color: transparent;
          .v-tab{
            color: #508DA3;
            opacity: .8;
            font-weight: 400 !important;
            letter-spacing: 1px;
            font-size: 1.25rem !important;
            text-shadow: -2px 2px 4px rgba(0,0,0,.35),
            2px -2px 3px rgba(255,255,255,.6),
            1px -1px 1px rgba(255,255,255,.6),
            -1px 1px 1px rgba(0,0,0,.35);
          }
        }
      }
      
    }
    .v-main{
      width: 100%;
    }
  }
}

</style>

