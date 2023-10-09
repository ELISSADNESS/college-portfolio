import React from "react";

import Button from "../button/button";

import styles from "./main.module.css";

function Main(){
    return(
        <>
            <div className={styles.container}>
                <div className={styles.works}>
                    <img src="" />
                    <img src="" />
                    <img src="" />
                    <img src="" />
                    <img src="" />
                    <img src="" />
                </div>
            </div>
            <div className={styles.btnCenter}>
                <Button>1</Button>
                <Button>2</Button>
                <Button>3</Button>
                <Button>4</Button>
            </div>
        </>
    );
}

export default Main;