function wordCount(myString) {
    var stringArray = myString.split(" ");
    var frequency = {};
    for (var i = 0; i<stringArray.length; i++){
        var currentCount = stringArray[i];
        if (currentCount in frequency) {
            frequency[currentCount]+=1;
        }
        else {
            // Set the counter at 1
            frequency[currentCount] = 1;
          }
        }
        console.log(frequency);
        return frequency;
      }
      
      wordCount("I yam what I yam and always will be what I yam"); 
 