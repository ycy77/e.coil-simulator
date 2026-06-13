---
entity_id: "protein.P37596"
entity_type: "protein"
name: "norW"
source_database: "UniProt"
source_id: "P37596"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "norW flrR ygbD b2711 JW2681"
---

# norW

`protein.P37596`

## Static

- Type: `protein`
- Source: `UniProt:P37596`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: One of at least two accessory proteins for anaerobic nitric oxide (NO) reductase. Reduces the rubredoxin moiety of NO reductase. The CPLX0-1 NorV/NorW system constitutes a nitric oxide reductase that couples NADH oxidation to NO reduction . The electron transfer chain begins with NADH oxidation by NorW, which then transfers the electron to the rubredoxin domain of NorV. Electrons travel through the protein to the catalytic di-iron site, where they are used for reduction of NO to N2O. NorW is a flavorubredoxin reductase that converts the oxidized form of the flavorubredoxin (NorV) electron carrier to its reduced form . The redox properties of NorW have been characterized , and the kinetics of electron transfer from NADH via NorW and NorV to NO has been measured . Partially purified NorW also shows some tellurite reductase activity with NADH as the electron donor . Nitric oxide has been shown to have diverse biologial functions; however, the molecule also inactivates essential cellular enzymes. It is therefore essential that NO is removed from the cell. A kinetic model of the fate of NO within E. coli has been constructed and tested. EG10456-MONOMER Hmp appears to be the major NO sink both aerobically and under microaerophilic conditions, with an increasing role for the NorVW NO reductase system when Hmp becomes unavailable...

## Biological Role

Catalyzes RXN-22001 (reaction.ecocyc.RXN-22001). Bound by FAD (molecule.C00016).

## Annotation

FUNCTION: One of at least two accessory proteins for anaerobic nitric oxide (NO) reductase. Reduces the rubredoxin moiety of NO reductase.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22001|reaction.ecocyc.RXN-22001]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2711|gene.b2711]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37596`
- `KEGG:ecj:JW2681;eco:b2711;ecoc:C3026_14920;`
- `GeneID:947088;`
- `GO:GO:0005737; GO:0015044; GO:0016491; GO:0016731; GO:0046210; GO:0050660; GO:0071732`
- `EC:1.18.1.-`

## Notes

Nitric oxide reductase FlRd-NAD(+) reductase (EC 1.18.1.-) (Flavorubredoxin reductase) (FlRd-reductase) (FlavoRb reductase)
