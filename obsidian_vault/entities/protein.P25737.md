---
entity_id: "protein.P25737"
entity_type: "protein"
name: "lysP"
source_database: "UniProt"
source_id: "P25737"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7551055}; Multi-pass membrane protein {ECO:0000269|PubMed:7551055}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysP cadR b2156 JW2143"
---

# lysP

`protein.P25737`

## Static

- Type: `protein`
- Source: `UniProt:P25737`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7551055}; Multi-pass membrane protein {ECO:0000269|PubMed:7551055}.

## Enriched Summary

FUNCTION: Permease involved in lysine uptake (PubMed:1315732, PubMed:24056175). In addition, functions as a lysine sensor that mediates the lysine-dependent regulation of the transcriptional activator CadC (PubMed:18086202, PubMed:24056175). In the absence of lysine, or at low lysine concentrations, LysP inhibits CadC by an interaction with the transmembrane domain of CadC. In the presence of lysine, LysP loses its ability to interact with and inhibit CadC, and acts as a lysine permease (PubMed:18086202, PubMed:24056175). {ECO:0000269|PubMed:1315732, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:24056175}. LysP is a lysine-specific transporter which mediates the uptake of lysine for biosynthetic purposes and functions as a co-sensor for lysine in the lysine dependent acid-resistance (LDAR) system*. lysP encodes a lysine-specific transporter which contributes to lysine uptake when cells are grown aerobically at neutral pH; LysP mediated lysine uptake increases under anaerobic conditions in media of low pH with added lysine . lysP insertion mutants are resistant to the lysine analog, thialysine and lack lysine specific transport when cells are grown aerobically in nutrient rich YT medium...

## Biological Role

Catalyzes L-lysine:proton symport (reaction.ecocyc.TRANS-RXN-58). Transports L-Lysine (molecule.C00047), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Permease involved in lysine uptake (PubMed:1315732, PubMed:24056175). In addition, functions as a lysine sensor that mediates the lysine-dependent regulation of the transcriptional activator CadC (PubMed:18086202, PubMed:24056175). In the absence of lysine, or at low lysine concentrations, LysP inhibits CadC by an interaction with the transmembrane domain of CadC. In the presence of lysine, LysP loses its ability to interact with and inhibit CadC, and acts as a lysine permease (PubMed:18086202, PubMed:24056175). {ECO:0000269|PubMed:1315732, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:24056175}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-58|reaction.ecocyc.TRANS-RXN-58]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2156|gene.b2156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25737`
- `KEGG:ecj:JW2143;eco:b2156;ecoc:C3026_12085;`
- `GeneID:75206409;946667;`
- `GO:GO:0003333; GO:0005886; GO:0015171; GO:0015189; GO:0016020; GO:0042802; GO:0043200; GO:0097639`

## Notes

Lysine-specific permease LysP (Lysine transporter LysP) (Trigger transporter LysP)
