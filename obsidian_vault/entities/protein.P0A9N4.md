---
entity_id: "protein.P0A9N4"
entity_type: "protein"
name: "pflA"
source_database: "UniProt"
source_id: "P0A9N4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pflA act b0902 JW0885"
---

# pflA

`protein.P0A9N4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9N4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Activation of pyruvate formate-lyase 1 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. Under anaerobic conditions, pyruvate formate-lyase activating enzyme (PflA, PFL-AE) activates PYRUVFORMLY-MONOMER by generating an essential glycyl radical within the enzyme . PFL-AE belongs to the radical SAM superfamily of proteins . The enzyme is also capable of activating the tdcE-encoded KETOBUTFORMLY-INACT-MONOMER and EG11784-MONOMER . PFL-AE uses S-adenosylmethionine (SAM) and reduced flavodoxin as co-substrates to produce the glycyl radical, generating 5'-deoxyadenosine and methionine as side products. The pro-S hydrogen from Gly734 in pyruvate formate-lyase is abstracted by the 5'-deoxyadenosyl radical in the active site of PFL-AE and incorporated into 5'-deoxyadenosine . The interaction of the enzyme with SAM and the mechanism of radical generation has been investigated . Formation of an organometallic intermediate, Ω, which consists of an Fe-C5' bond between the 5'-deoxyadenosyl radical and the [4Fe4S] cluster, is central to catalysis . A monovalent cation (M+), likely K+, binds within the active site, where it interacts with SAM and controls reactivity . A redox-interconvertible [4Fe-4S] cluster is essential for interaction with SAM...

## Biological Role

Catalyzes protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving) (reaction.R04710), 1.97.1.4-A-RXN (reaction.ecocyc.1.97.1.4-A-RXN), TDCEACT1-RXN (reaction.ecocyc.TDCEACT1-RXN). Bound by Potassium cation (molecule.C00238), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Activation of pyruvate formate-lyase 1 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - via EC:1.97.1.4
- `catalyzes` --> [[reaction.ecocyc.1.97.1.4-A-RXN|reaction.ecocyc.1.97.1.4-A-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TDCEACT1-RXN|reaction.ecocyc.TDCEACT1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0902|gene.b0902]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9N4`
- `KEGG:ecj:JW0885;eco:b0902;ecoc:C3026_05570;`
- `GeneID:86863427;93776516;945517;`
- `GO:GO:0005829; GO:0006006; GO:0006974; GO:0016491; GO:0030955; GO:0043365; GO:0051539; GO:0051604`
- `EC:1.97.1.4`

## Notes

Pyruvate formate-lyase 1-activating enzyme (EC 1.97.1.4) (Formate-C-acetyltransferase-activating enzyme 1) (PFL-activating enzyme 1)
