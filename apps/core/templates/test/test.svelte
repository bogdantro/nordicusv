

<script type="text/javascript">
    const test = 'aaaaaaa';
</script>

<div class="test">
    <div class="dropdown"></div>
    <button onclick="test()">{test}</button>
</div>

<br>
<h1>{test}</h1>

<style>
    .test{
        width: 50%;
        height: 50px;
        background: black;
    }
    .dropdown{
        width: 30%;
        height: 60px;
        background: red;
        display: none;
    }
    .dropdown .active{
        display: block;
    }
</style>
