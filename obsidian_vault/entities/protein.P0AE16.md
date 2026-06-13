---
entity_id: "protein.P0AE16"
entity_type: "protein"
name: "ampG"
source_database: "UniProt"
source_id: "P0AE16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15728916, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15728916}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ampG b0433 JW0423"
---

# ampG

`protein.P0AE16`

## Static

- Type: `protein`
- Source: `UniProt:P0AE16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15728916, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15728916}.

## Enriched Summary

FUNCTION: Permease involved in cell wall peptidoglycan recycling (PubMed:12426329, PubMed:8878601). Transports, from the periplasm into the cytoplasm, the disaccharide N-acetylglucosaminyl-beta-1,4-anhydro-N-acetylmuramic acid (GlcNAc-anhMurNAc) and GlcNAc-anhMurNAc-peptides (PubMed:12426329). Transport is dependent on the proton motive force (PubMed:12426329). AmpG is also involved in beta-lactamase induction (PubMed:7773404). {ECO:0000269|PubMed:12426329, ECO:0000269|PubMed:7773404, ECO:0000269|PubMed:8878601}. AmpG encodes an anhyhyro-muropeptide transporter required for peptidoglycan recycling. In many enterobacteria (but not E. coli) AmpG participates in an EG10040-MONOMER AmpC induction pathway (see ). ampG is required for the induction of β-lactam resistance in an E. coli strain engineered for inducible β-lactamase activity (strain SN0301/pNU305) . ampG mutants are defective in peptidoglycan recycling and release muropeptides (GlnNAc-anhydoMurNAc-tetrapeptide and tetrapeptide) into the culture medium; AmpG is a muropeptide-specific permease required for peptidoglycan recycling (see also . AmpG transports anhydro-muropeptides specifically and transport is dependent on the proton motive force...

## Biological Role

Catalyzes TRANS-RXN-1570 (reaction.ecocyc.TRANS-RXN-1570), TRANS-RXN-1571 (reaction.ecocyc.TRANS-RXN-1571), muropeptide:proton symport (reaction.ecocyc.TRANS-RXN0-226), muropeptide:proton symport (reaction.ecocyc.TRANS-RXN0-258). Transports hν (molecule.ecocyc.Light).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

FUNCTION: Permease involved in cell wall peptidoglycan recycling (PubMed:12426329, PubMed:8878601). Transports, from the periplasm into the cytoplasm, the disaccharide N-acetylglucosaminyl-beta-1,4-anhydro-N-acetylmuramic acid (GlcNAc-anhMurNAc) and GlcNAc-anhMurNAc-peptides (PubMed:12426329). Transport is dependent on the proton motive force (PubMed:12426329). AmpG is also involved in beta-lactamase induction (PubMed:7773404). {ECO:0000269|PubMed:12426329, ECO:0000269|PubMed:7773404, ECO:0000269|PubMed:8878601}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1570|reaction.ecocyc.TRANS-RXN-1570]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1571|reaction.ecocyc.TRANS-RXN-1571]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-226|reaction.ecocyc.TRANS-RXN0-226]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-258|reaction.ecocyc.TRANS-RXN0-258]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0433|gene.b0433]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE16`
- `KEGG:ecj:JW0423;eco:b0433;ecoc:C3026_02115;`
- `GeneID:75170451;946438;`
- `GO:GO:0005886; GO:0009254; GO:0015293; GO:0015647; GO:0071555`

## Notes

Anhydromuropeptide permease (AmpG permease) (Muropeptide:H(+) symporter)
