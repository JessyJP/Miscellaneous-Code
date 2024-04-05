function dzdt = lorenzSystem(t, r, sigma, rho, beta)
    % Extract the current state
    x = r(1);
    y = r(2);
    r = r(3);

    % Lorenz system differential equations
    dxdt = sigma * (y - x);
    dydt = x * (rho - r) - y;
    dzdt = x * y - beta * r;

    % Return the derivatives as a column vector
    dzdt = [dxdt; dydt; dzdt];
end
