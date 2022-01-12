<template>
  <div class="home">
    <h1 class="header">White Eagle Martial Arts</h1>
    <h2 class="tagline">Healing Lives through Martial Arts</h2>
    <div class="headerGroup">
      <h3>Strengthen The Body</h3>
      <h3>Train The Mind</h3>
      <h3>Develop the Spirit</h3>
    </div>
    <div class="classPhoto">
      <img src="../assets/classPhoto.jpg" alt=""/>
    </div> 
    <div class="announcements">
      <div class="announcements-card">
        <h3>Announcements</h3>
    </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {
  },
};
</script>
<style lang="scss">
.home{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: calc(100vh - 15rem);
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
    color: rgba(255, 255, 255, 0.88);
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
    margin-left: 100px;
    margin-top: 3rem;
    font-size: 3rem;
    opacity: .8;
    color: #A5DEF1;
    letter-spacing: 9px;
    text-shadow: 
      -2px 2px 4px rgb(29 38 50 / 35%), 
      2px -2px 4px rgb(205 228 255 /25%), 
      1px -1px 3px rgb(205 228 255 / 25%),
      -1px 1px 3px rgb(29 38 50 / 35%);
    
    font-weight: 100;
    z-index: 10;
  }
  .headerGroup{
    margin: 1rem 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    
    z-index: 10;
    h3{
      color: white;
      font-weight: 100;
      letter-spacing: 10px;
      font-size:1rem;
      text-align: center;
      margin: 1rem;
      text-shadow: -5px 19px 3px rgba(255,255,255,.19);

    }
  }
  .classPhoto{
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 1rem;
    margin-bottom: 15rem;
    z-index: 10;
    img{
      max-width:100%; 
      max-height: 35vh;
      margin: auto;
      border-radius: 5px;
      border: 1px solid rgba(0, 0, 0, 0.712);
      box-shadow: 3px -3px 8px rgba(90, 122, 171, 0.603), 
        1px -1px 2px rgba(90, 122, 171, 0.603), 
        -3px 3px 20px rgb(26 31 40 / 54%), 
        -1px 1px 2px rgb(26 31 40 / 54%) !important;
    };
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
        -3px 3px 20px rgb(43 56 76 / 47%), 
        -1px 1px 2px rgb(43 56 76 / 47%), 
        inset -2px 2px 10px rgb(180 194 217 / 55%), 
        inset 2px -2px 7px rgb(56 67 86 / 54%) !important;
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
</style>
