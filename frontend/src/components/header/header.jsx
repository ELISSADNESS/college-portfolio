import React from "react";

import Button from "../button/button";

import styles from "./header.module.css";

function Header() {
    return (
        <>
            <div className={styles.navBtn}>
                <Button>Все работы</Button>
                <Button>Иллюстрации</Button>
                <Button>Фото</Button>
                <Button>Шрифты</Button>
            </div>

            <h1 className={styles.title}>Работы<br />студентов</h1>
        </>
    );
}

export default Header;