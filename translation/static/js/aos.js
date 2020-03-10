async function myfunction(msg1, msg2, msg3){
        document.getElementById('loading').style.display='block';
        var para = document.forms["form"]["para"].value;
        var lines = para.split('.');
        var i;
        document.getElementById('demo').innerHTML=lines.length();
        for(i=0; i<lines.length(); i++)
        {
            document.getElementById('demo').innerHTML=msg1;
            await sleep(4000);
            document.getElementById('demo').innerHTML=msg2;
            await sleep(3000);
            document.getElementById('demo').innerHTML=msg3;
            await sleep(3000);
        }
    }

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}