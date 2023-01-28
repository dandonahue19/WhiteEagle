<template>
  <v-app>
    <div class="wema">
      <div class="home">
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
        <div class="mobileNav">
          <div class="logo rounded-circle">
            <img  src="./assets/wemaLogo.png"/>
          </div>
          <v-btn to="/about" plain class="navItem">
            <v-icon>mdi-information-outline</v-icon>
            <p>ABOUT</p>
          </v-btn>
          <v-btn to="/calendar" plain class="navItem">
            <v-icon>mdi-calendar-month</v-icon>
            <p>CALENDAR</p>
          </v-btn>
          <v-btn to="/tuition" plain class="navItem">
            <v-icon>mdi-currency-usd</v-icon>
            <p>TUITION</p>
          </v-btn>
        </div>
        <v-main>
          <router-view></router-view>
        </v-main>
      </div>
    </div>
      
    
  </v-app>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      tab: 0
    }
  },
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
  .home{
    margin-top: 6rem;
    margin-bottom: 6rem;
    width: 1250px;
    position: relative;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    background-color: #2a3950;
    box-shadow: 3px -3px 68px rgba(255, 255, 255, 0.3), 
      1px -1px 4px rgba(204, 198, 198, 0.3), 
      inset -2px 2px 15px rgba(255, 255, 255, 0.2), 
      inset 2px -2px 15px rgb(139 161 169 / 20%), 
      -3px 3px 20px rgb(139 161 169 / 40%), 
      -1px 1px 2px rgb(139 161 169 / 40%) !important;
    .logo{
      position: absolute;
      z-index: 999;
      left: 0;
      top: -7rem;
      margin: 1rem;
      width: 200px;
      height: 200px;
      opacity: .95;
      
      img{
        width: 100%;
        height: 100%;
        border-radius: 200px;
        box-shadow: 3px -3px 6px rgba(255, 255, 255, 0.4), 
          1px -1px 2px rgba(255, 255, 255, 0.5), 
          inset -2px 2px 10px rgba(255, 255, 255, 0.212), 
          -3px 3px 6px rgba(0, 0, 0, 0.3), 
          -1px 1px 2px rgba(0, 0, 0, 0.4);
        }
    }
    .mobileNav{
      display: none;
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
@media(max-width: 1000px){
  .wema{
    padding: 0;
    .home{
      height: 100vh;
      margin-top:0rem;
      margin-bottom: 0;
      border-radius: 0;
      .logo{
        display:none;
      }
      .nav{
        display: none;
      }
      .mobileNav{
        height: 75px;
        display: block;
        position: absolute;
        bottom: 0rem;
        left:0;
        width: 100vw;
        padding: .5rem 0;
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: white;
        padding-left: 110px;
        z-index: 99999;
        .logo{
          display: block;
          width: 125px;
          height: 125px;
          top: unset;
          margin: 0;
          bottom: 0.5rem;
          left: 0.5rem;
          img{
            box-shadow: none;
          }
        }
        .navItem{
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 0;
          height: 75px;
          border-radius: 0;
          width: 33%;
          &:nth-child(3){
            border-left: 1px solid #00000036;
            border-right: 1px solid #00000036;
          }
          .v-btn__content{
            flex-direction: column;
          }
          p{
            margin: 0;
            font-weight: bold;
            font-size: 0.7rem;
            opacity: 0.7;
          }
          .v-icon{
            font-size: 2rem;
          }
        }
      }
      .v-main{
        height: calc(100vh - 70px);
      }
    }
  }
}

</style>

