---
entity_id: "complex.ecocyc.CPLX0-7655"
entity_type: "complex"
name: "maltose outer membrane channel / phage lambda receptor protein"
source_database: "EcoCyc"
source_id: "CPLX0-7655"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-OUTER-MEM-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "maltoporin"
---

# maltose outer membrane channel / phage lambda receptor protein

`complex.ecocyc.CPLX0-7655`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7655`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-OUTER-MEM-GN
- Complex type: `structural`
- Components: [[protein.P02943|protein.P02943]]

## Enriched Summary

LamB is a trimeric outer membrane protein which facilitates the specific diffusion of maltose and longer maltooligosaccharides across the outer membrane; it also acts as a non-specific porin for small hydrophilic molecules and as a receptor for various bacteriophages (see and further references within). Early work (in various E. coli K-12 strains including HfrG6, W3110, and CR63) characterized lamB mutations which impaired adsorption of bacteriophage λ and caused defects in maltose transport . LamB mutants are unable to grow on maltodextrins but can still grow on maltose (Dex- Mal+) ; the general porin channels OmpF and OmpC support diffusion of maltose although at a slower rate than LamB. LamB has a poor affinity for maltose, isomaltose and cyclic dextrin and an increasing affinity for longer maltooligosaccharides . LamB functions as a saturable channel for maltooligosaccharide - diffusion of the maltohexaose analog, CPD-27111, displays Michaelis-Menten kinetics . LamB contributes to trehalose uptake; LamB is required for the efficient uptake of trehalose at low substrate concentrations (see also ). LamB may function as a broad specificity glycoporin in low nutrient environments; LamB confers a competitive growth advantage under carbohydrate-limiting conditions in chemostats...

## Biological Role

Catalyzes RXN0-1741 (reaction.ecocyc.RXN0-1741), RXN0-1804 (reaction.ecocyc.RXN0-1804).

## Annotation

LamB is a trimeric outer membrane protein which facilitates the specific diffusion of maltose and longer maltooligosaccharides across the outer membrane; it also acts as a non-specific porin for small hydrophilic molecules and as a receptor for various bacteriophages (see and further references within). Early work (in various E. coli K-12 strains including HfrG6, W3110, and CR63) characterized lamB mutations which impaired adsorption of bacteriophage λ and caused defects in maltose transport . LamB mutants are unable to grow on maltodextrins but can still grow on maltose (Dex- Mal+) ; the general porin channels OmpF and OmpC support diffusion of maltose although at a slower rate than LamB. LamB has a poor affinity for maltose, isomaltose and cyclic dextrin and an increasing affinity for longer maltooligosaccharides . LamB functions as a saturable channel for maltooligosaccharide - diffusion of the maltohexaose analog, CPD-27111, displays Michaelis-Menten kinetics . LamB contributes to trehalose uptake; LamB is required for the efficient uptake of trehalose at low substrate concentrations (see also ). LamB may function as a broad specificity glycoporin in low nutrient environments; LamB confers a competitive growth advantage under carbohydrate-limiting conditions in chemostats . Monomeric LamB is an 18-stranded antiparallel β-barrel that forms a water-filled channel with a central constriction; a hydrophobic path composed of aromatic amino acid residues (the so-called 'greasy slide') located at the channel lining and two 'ionic tracks' (composed of acidic and basic residues) located at the channel constriction form the sugar translocation pathway (see also and further ). LamB has been extensively mutated to probe the determinants of sugar binding and phage adsorption and

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1741|reaction.ecocyc.RXN0-1741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1804|reaction.ecocyc.RXN0-1804]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P02943|protein.P02943]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:CPLX0-7655`
- `QSPROTEOME:QS00183237`

## Notes

3*protein.P02943
