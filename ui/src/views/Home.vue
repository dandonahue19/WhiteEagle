<template>
  <div class="welcome">
    <div class="headerGroup">
      <div class="imageCard">
        <img src="../assets/strength.jpg" alt=""/>
        <h3>Strengthen The Body</h3>
      </div>
      <div class="imageCard">
        <img src="../assets/mind.jpg" alt=""/>
        <h3>Train The Mind</h3>
      </div>
      <div class="imageCard">
        <img src="../assets/spirit.jpg" alt=""/>
        <h3>Develop the Spirit</h3>
      </div>
    </div>
    <h2 class="tagline">Healing Lives Through Martial Arts</h2>
<!--    <div class="watermark">-->
<!--      <img  src="../assets/trees.jpg"/>-->
<!--      <div class="gradient"></div>-->
<!--    </div>-->

<!--    <div class="announcements">-->
<!--      <div class="announcements-card">-->
<!--        <h3>Announcements</h3>-->
<!--        <div class="announcement" v-for="announcement in announcements" :key="announcement.id">-->
<!--          <h4>{{announcement.name}}</h4>-->
<!--          <p>{{announcement.description}}</p>-->
<!--        </div>-->
<!--    </div>-->
<!--    </div>-->
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {
  },
  data() {
    return{
      announcements:[]
    }
  },
  created(){
    let  query = `{
      announcements{
        name
        description
      }
    }`
    this.$axios.get('graphql', {params:{query}}).then((res) => {
      console.log(res.data)
      this.announcements = res.data.data.announcements
    })
  }
};
</script>
<style lang="scss">
.welcome{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: calc(100% - 15rem);
  position: absolute;
  width: 100%;
  &::before {    
      content: "";
      background-image: url('../assets/trees.jpg');
      background-size: cover;
      border-radius: 5px;
      position: absolute;
      top: 0px;
      left: 0rem;
      width: 100%;
      height: 100%;
      opacity: 0.045;
      z-index: 1;
  } 
  .header{
    color: rgba(255, 255, 255, 0.9);
    margin-left: calc(200px + 3rem);
    margin-top: 1rem;
    font-size: 3rem;
    letter-spacing: 5px;
    font-weight: 500;
    font-family: Roboto;
    text-transform: uppercase;
    z-index: 10;
  }
  .tagline{
    background: white;
    margin-top: 3rem;
    padding: 1rem;
    font-size: 3rem;
    opacity: .95;
    color: #000000ba;
    letter-spacing: 9px;
    text-shadow: 
      -2px 2px 4px rgb(29 38 50 / 25%),
      2px -2px 4px rgb(205 228 255 /15%),
      1px -1px 3px rgb(205 228 255 / 15%),
      -1px 1px 3px rgb(29 38 50 / 25%);
    text-align: center;
    font-weight: 100;
    z-index: 10;
  }
  .headerGroup{
    margin: 1rem 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    z-index: 10;
    .imageCard{
      position: relative;
      min-width: 400px;
      max-width: 30%;
      margin: 1rem;
      h3{
        border-radius: 5px;
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 1rem;
        color: white;
        font-weight: 100;
        letter-spacing: 8px;
        font-size:1rem;
        text-align: center;
        text-shadow: -5px 19px 3px rgba(255,255,255,.19);
        background: #000000a6;
      }
      img{
        max-width: 30vw;
        width: calc(100% - 4rem);
        border-radius: 4px;
        margin: 1rem 2rem;
      }
    }

  }
  .watermark{

    width: 100%;
    position: fixed;
    bottom: 0;
    img{
      width: 100%;
      opacity: .1;
    }
    .gradient{
      position:absolute;
      z-index:2;
      right:0; bottom:0; left:0;
      height:200px;
      background: linear-gradient(to top,  rgba(255,255,255,0) 0%,rgba(255,255,255,1) 70%);
    }
  }

  .announcements{
    background-color: white;
    position: absolute;
    bottom: -4rem;
    display: flex;
    justify-content: center;
    width: 100%;
    z-index: 10;
    .announcements-card{
      background-color: #8492a9;
      color: white;
      position: absolute;
      bottom: 0;
      margin: auto;
      margin-top:3rem;
      height: 19vh;
      width: 75vw;
      max-width: 1000px;
      border-radius: 5px;
      box-shadow: 3px -3px 8px #dbe9ff17, 
        1px -1px 2px #dbe9ff17, 
        -3px 3px 20px rgb(43 56 76 / 30%), 
        -1px 1px 2px rgb(43 56 76 / 30%), 
        inset -2px 2px 10px rgb(180 194 217 / 30%), 
        inset 2px -2px 7px rgb(56 67 86 / 30%) !important;
        text-align: center;
        h3{
          font-size:1.5rem;
          padding-bottom: .5rem;
          margin: 1rem;
          border-bottom: 1px solid rgba(255,255,255,.4);
        }
    }
  }
}
@media(max-width: 1000px){
  .welcome{
    height: 100%;
    .header{
      margin-left: 0;
      margin-top: 0;
      padding: 1rem0.5rem;
      font-size: 2.25rem;
      text-align: center;
      color: #ffffff;
      background: #cb2b2beb;
      height: 20%;
      display: flex;
      align-items: center;
    }
    .tagline{
      font-size: 1.25rem;
      margin-top: 0rem;
      margin-left: 0rem;
      padding: 1rem;
      background: #121b26;
      text-align: center;
    }
    .headerGroup{
      flex-direction: column;
      order: 4;
      margin: 0;
      h3{
        letter-spacing: 7px;
        font-size: 1rem;
        text-align: center;
        margin: 0.5rem;
        text-shadow: 1px 17px 4px rgb(255 255 255 / 29%);
      }
    }
    .classPhoto{
      margin-top: 0;
      margin-bottom: 0;
      order: 3;
      img{
        border-radius: 0;
      }
      
    }
    .announcements{
      position: relative;
      width: 100%;
      order: 5;
      bottom: 0;
      height: 15%;
      .announcements-card{
        position: relative;
        height: 100%;
        width: 100%;
        border-radius: 0;
        margin-top:0;
        h3{
          border-bottom: none;
          font-size: 1rem;
          padding-bottom: 0.5rem;
          margin: 0.5rem;
        }
      }
    }
  }
}
</style>
