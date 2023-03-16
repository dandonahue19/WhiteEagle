<template>
  <v-app>
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <div class="wema">
      <div class="home">

        <div class="nav">
          <v-tabs v-model="tab" centered>
            <v-tab to="/">Welcome</v-tab>
            <v-tab to="/about">Info</v-tab>
            <v-tab class="placeholder"></v-tab>
            <v-tab to="/calendar">Calendar</v-tab>
            <v-tab>Tuition</v-tab>
          </v-tabs>
          <div class="logo rounded-circle">
            <img  src="./assets/wemaLogo.png"/>
          </div>
        </div>
        <div class="mobileNav" :style="{'top': (vh-75)+'px'}">
          <router-link to="/" tag="div" class="logo rounded-circle">
            <img  src="./assets/wemaLogo.png"/>
          </router-link>
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
      tab: 0,
      vh: window.visualViewport.height,
    }
  },
  created(){
    
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    })
  },
  beforeDestroy() { 
    window.removeEventListener('resize', this.onResize); 
  },
  methods: {  
    onResize() {
      this.vh = window.visualViewport.height;
    }
  }
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
html{
  height:100%
}
body{
  height: 100%;
  background-color: #d1e3e9;
}
.v-main{
  z-index: 9999
}
.wema{
  height: 100%;
  width: 100vw;
  display: flex;
  justify-content: center;
  .home{
    width: 100%;
    position: relative;
    // background-color: #2a3950;
    background-color: #131d28;
    .logo{
      z-index: 999;
      width: 200px;
      height: 200px;
      margin: auto;
      margin-top: -125px;
      img {
        width: 100%;
        height: 100%;
        border-radius: 200px;
      }
    }
    .mobileNav{
      display: none;
      transition: all .1s;
    }
    .nav{
      width: 100%;
      margin-top: 100px;
      .v-tabs{
        background: white;
        .v-tabs-bar{
          background-color: transparent;
          .v-tab{
            color: #000000ba;
            width: 135px;
            opacity: .8;
            font-weight: 600 !important;
            letter-spacing: 1px;
            font-size: 1.25rem !important;
            &.placeholder{
              width: 225px;
            }
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
      height: 100%;
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

