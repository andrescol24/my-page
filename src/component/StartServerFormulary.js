import { useState } from "react";
import { startMinecraftServer } from "../api";
import { Spinner } from "react-bootstrap";

function StartServerFormulary({updateStatus}) {
    const [user, setUser] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const startServer = (event) => {
        event.preventDefault();
        setError(null);
        setLoading(true);
        startMinecraftServer(
            {user, password},
            handleSuccess,
            handleError
        )
    }

    const handleError = (error) => {
        setLoading(false);
        setError(error);
    }

    const handleSuccess = (json) => {
        setLoading(false);
        updateStatus(json);
    }

    const handleUserChange = (event) => {
        setUser(event.target.value);
    }
    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
    }

    return (
        <form>
            <h6 className="text-center alert alert-danger">Hay que iniciar el servidor por que nadie esta jugando</h6>
            <div className="form-group">
                <label>Usuario </label>
                <input type="text" className="form-control" 
                    id="user" onChange={handleUserChange} placeholder="Ya usted sabe parce..." />
            </div>
            <div className="form-group">
                <label>Contraseña</label>
                <input type="password" className="form-control" 
                    id="password" onChange={handlePasswordChange} placeholder="Ojo pues..." />
                <small id="emailHelp" className="form-text text-muted">No la compartas, lo veo todo!</small>
            </div>

            {error && 
            <div className="alert alert-danger" role="alert">
                Uy parce fallo el inicio, revisa bien la Contraseña o escribame!
            </div>}

            {loading &&
            <Spinner animation="border"/>}<br/>
            
            <button className="btn btn-primary" disabled={!user || !password }onClick={startServer}>Iniciar</button>
        </form>
    );
}
export default StartServerFormulary;