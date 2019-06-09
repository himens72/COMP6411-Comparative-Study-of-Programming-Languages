(require ['clojure.string :as 'str])

(defn readFile []    
  (def lines (slurp "map.txt"))    
  (clojure.string/split lines #"\r?\n")    
  (println "This is my challenger : ")
  (println lines)
  (def columns (count (get (clojure.string/split lines #"\r?\n") 0)))
  (def rows (count (clojure.string/split lines #"\r?\n"))))

(defn mapValidity[]
  (loop [x 0]
      (when (< x rows)
         (if (not= (count (get (clojure.string/split lines #"\r?\n") x)) columns)
           (do
             (println "Input File is Not Valid")
             (System/exit 0)))
         (recur (+ x 1)))))

(defn visited[]
  (def adjacentData (make-array Integer/TYPE (* rows columns) 4))
  (loop [x 0]        
    (when (< x rows)            
      (def currentLine (get (clojure.string/split lines #"\r?\n") x)) 
      (loop [y 0]        
        (when (< y columns)           
          (def index (+ y (* columns x)))
          (aset-int adjacentData index 0  -1)          
          (aset-int adjacentData index 1  -1)          
          (aset-int adjacentData index 2  -1)          
          (aset-int adjacentData index 3  -1)
          (cond
            (= index 0) (do (aset-int adjacentData index 0  -1)(aset-int adjacentData index 3  -1)(aset-int adjacentData index 1  (+ (+ y 1) (* columns x))) (aset-int adjacentData index 2  (+ y (* columns (+ x 1)))))
            (= index (- columns 1))(do (aset-int adjacentData index 0  -1)(aset-int adjacentData index 1  -1)(aset-int adjacentData index 2  (+ y (* columns (+ x 1)))) (aset-int adjacentData index 3  (+ (- y 1) (* columns x))))
            (= index (* columns (- rows 1))) (do (aset-int adjacentData index 2  -1)(aset-int adjacentData index 3  -1)(aset-int adjacentData index 0  (+ y (* columns (- x 1)))) (aset-int adjacentData index 1  (+ (+ y 1) (* columns x))))
            (= index (- (* rows columns) 1)) (do (aset-int adjacentData index 1  -1)(aset-int adjacentData index 2  -1)(aset-int adjacentData index 3  (+ (- y 1) (* columns x))) (aset-int adjacentData index 0  (+ y (* columns (- x 1)))))
            (= (/ index columns) 0) (do (aset-int adjacentData index 0  -1)(aset-int adjacentData index 1  (+ (+ y 1) (* columns x))) (aset-int adjacentData index 2  (+ y (* columns (+ x 1))))(aset-int adjacentData index 3  (+ (- y 1) (* columns x))))
            (= (mod (+ index 1) columns) 0)(do (aset-int adjacentData index 1  -1)(aset-int adjacentData index 3  (+ (- y 1) (* columns x))) (aset-int adjacentData index 2  (+ y (* columns (+ x 1))))(aset-int adjacentData index 0  (+ y (* columns (- x 1)))))
            (= (mod index columns) 0)(do (aset-int adjacentData index 3  -1)(aset-int adjacentData index 0  (+ y (* columns (- x 1))))(aset-int adjacentData index 1  (+ (+ y 1) (* columns x)))(aset-int adjacentData index 2  (+ y (* columns (+ x 1)))))
            (> index (* columns (- rows 1)))(do (aset-int adjacentData index 2  -1)(aset-int adjacentData index 3  (+ (- y 1) (* columns x))) (aset-int adjacentData index 0  (+ y (* columns (- x 1))))(aset-int adjacentData index 1  (+ (+ y 1) (* columns x))))
            :else (do (aset-int adjacentData index 0  (+ y (* columns (- x 1))))(aset-int adjacentData index 1  (+ (+ y 1) (* columns x))) (aset-int adjacentData index 2  (+ y (* columns (+ x 1))))(aset-int adjacentData index 3  (+ (- y 1) (* columns x)))))    
          (def destinationLine (get (clojure.string/split currentLine #"") y))
          (case destinationLine "@" (def destination index) (def nodestination -1))
          (recur (+ y 1))))           
      (recur (+ x 1)))))

(defn printOutput [visitedData, localPathList1, d1]
  (println "Woo hoo, I found the treasure :-)")
  (loop [x 0]        
    (when (< x rows)            
      (def tempCurrentLine (get (clojure.string/split lines #"\r?\n") x)) 
      (loop [y 0]        
        (when (< y columns)
          ;;(print (get tempCurrentLine y))
          (def tempIndex (+ y (* columns x)))
          (cond
            (= (get tempCurrentLine y) "#") (print "#")
            (= tempIndex d1) (print "@")
            (and (= (aget visitedData tempIndex 0) (aget localPathList1 tempIndex 0)) (= (aget visitedData tempIndex 0) 1)) (print "+")                
            (and (= (aget visitedData tempIndex 0) 0) (= (aget localPathList1 tempIndex 0) 1)) (print "!")
            :else (print (get tempCurrentLine y)))
          (recur (+ y 1))))
      (println "")
      (recur (+ x 1))))
  (System/exit 0))

(defn printPathUtils [s,d,visitedData,localPathList]
  (aset-int visitedData s 0 1)
  (if (= s d)
    (do
      (printOutput visitedData localPathList d)))
  (def a (mod (aget adjacentData s 0) columns))
  (def b (/ (- (aget adjacentData s 0) a) columns))
  (if(and (> (aget adjacentData s 0) -1) (and (and (< a columns) (> a -1)) (and (< b rows) (> b -1))))
    (do
      (def width (mod (aget adjacentData s 0) columns))
      (def height (/ (- (aget adjacentData s 0) width) columns))
      (def currentLine (get (clojure.string/split lines #"\r?\n") height)) 
      (def destinationLine (get (clojure.string/split currentLine #"") width))
      (if (or (= destinationLine "-") (= destinationLine "@"))
        (do 
          (if (= (aget visitedData (aget adjacentData s 0) 0) 0)
            (do
              (aset-int localPathList (aget adjacentData s 0) 0 1)
              (printPathUtils (aget adjacentData s 0) d visitedData, localPathList)
              (aset-int localPathList (aget adjacentData s 0) 0 1)))))))
  (def c (mod (aget adjacentData s 1) columns))
  (def e (/ (- (aget adjacentData s 1) c) columns))
  (if(and (> (aget adjacentData s 1) -1) (and (and (< c columns) (> c -1)) (and (< e rows) (> e -1))))
    (do
      (def width (mod (aget adjacentData s 1) columns))
      (def height (/ (- (aget adjacentData s 1) width) columns))
      (def currentLine (get (clojure.string/split lines #"\r?\n") height)) 
      (def destinationLine (get (clojure.string/split currentLine #"") width))
      (if (or (= destinationLine "-") (= destinationLine "@"))
        (do 
          (if (= (aget visitedData (aget adjacentData s 1) 0) 0)
            (do
              (aset-int localPathList (aget adjacentData s 1) 0 1)
              (printPathUtils (aget adjacentData s 1) d visitedData, localPathList)
              (aset-int localPathList (aget adjacentData s 1) 0 1)))))))
  (def f (mod (aget adjacentData s 2) columns))
  (def g (/ (- (aget adjacentData s 2) f) columns))
  (if(and (> (aget adjacentData s 2) -1) (and (and (< f columns) (> f -1)) (and (< g rows) (> g -1)))) 
    (do
      (def width (mod (aget adjacentData s 2) columns))
      (def height (/ (- (aget adjacentData s 2) width) columns))
      (def currentLine (get (clojure.string/split lines #"\r?\n") height)) 
      (def destinationLine (get (clojure.string/split currentLine #"") width))
      (if (or (= destinationLine "-") (= destinationLine "@"))
        (do 
          (if (= (aget visitedData (aget adjacentData s 2) 0) 0)
            (do
              (aset-int localPathList (aget adjacentData s 2) 0 1)
              (printPathUtils (aget adjacentData s 2) d visitedData, localPathList)
              (aset-int localPathList (aget adjacentData s 2) 0 1)))))))
  (def h (mod (aget adjacentData s 0) columns))
  (def i (/ (- (aget adjacentData s 0) h) columns))
  (if(and (> (aget adjacentData s 3) -1) (and (and (< h columns) (> h -1)) (and (< i rows) (> i -1))))
    (do
      (def width (mod (aget adjacentData s 3) columns))
      (def height (/ (- (aget adjacentData s 3) width) columns))
      (def currentLine (get (clojure.string/split lines #"\r?\n") height)) 
      (def destinationLine (get (clojure.string/split currentLine #"") width))
      (if (or (= destinationLine "-") (= destinationLine "@"))
        (do 
          (if (= (aget visitedData (aget adjacentData s 3) 0) 0)
            (do
              (aset-int localPathList (aget adjacentData s 3) 0 1)
              (printPathUtils (aget adjacentData s 3) d visitedData, localPathList)
              (aset-int localPathList (aget adjacentData s 3) 0 1)))))))        
  (aset-int visitedData s 0 0))
        

(defn printPath [s,d]
  (def visitedData (make-array Integer/TYPE (* rows columns) 1))
  (def pathList (make-array Integer/TYPE (* rows columns) 1))
  (aset-int pathList s 0 1)          
  (printPathUtils s d visitedData pathList)
  (println "Uh oh, I could not find the treasure :-(")
  (loop [x 0]        
    (when (< x rows)            
      (def tempCurrentLine (get (clojure.string/split lines #"\r?\n") x)) 
      (loop [y 0]        
        (when (< y columns)
          ;;(print (get tempCurrentLine y))
          (def tempIndex (+ y (* columns x)))
          (cond
            (= (get tempCurrentLine y) "#") (print "#")
            (= tempIndex destination) (print "@")
            (and (= (aget visitedData tempIndex 0) (aget pathList tempIndex 0)) (= (aget visitedData tempIndex 0) 1)) (print "+")                
            (and (= (aget visitedData tempIndex 0) 0) (= (aget pathList tempIndex 0) 1)) (print "!")
            :else (print (get tempCurrentLine y)))
          (recur (+ y 1))))
      (println "")
      (recur (+ x 1))))
  (System/exit 0))
  
(defn main[]    
  (readFile)
  (mapValidity)
  (visited) 
  (def start 0)
  (printPath start destination))

(main)
