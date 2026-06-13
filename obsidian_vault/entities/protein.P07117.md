---
entity_id: "protein.P07117"
entity_type: "protein"
name: "putP"
source_database: "UniProt"
source_id: "P07117"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:3007935, ECO:0000269|PubMed:3512540, ECO:0000269|PubMed:3902503, ECO:0000269|PubMed:9756872}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:9756872}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "putP b1015 JW1001"
---

# putP

`protein.P07117`

## Static

- Type: `protein`
- Source: `UniProt:P07117`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:3007935, ECO:0000269|PubMed:3512540, ECO:0000269|PubMed:3902503, ECO:0000269|PubMed:9756872}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:9756872}.

## Enriched Summary

FUNCTION: Catalyzes the sodium-dependent uptake of extracellular L-proline (PubMed:1567896, PubMed:3512540, PubMed:9693004). This protein is also capable of using lithium as the transport cation (PubMed:1567896, PubMed:9693004). Also catalyzes the uptake of propionate (PubMed:17088549). {ECO:0000269|PubMed:1567896, ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:3512540, ECO:0000269|PubMed:9693004}. PutP is a member of the SSS family of sodium/solute transporters . PutP is a sodium/proline symporter responsible for the uptake of proline. Mutations in putP decrease proline transport and can be complemented by the cloned putP gene . The PutP protein has been purified, reconstituted into proteoliposomes, and shown to mediate proline transport in the presence of a sodium or lithium ion gradient . Mutant phenotype and expression analysis also suggest that PutP may be responsible for the transport of the short chain fatty acid propionate . Kinetic analysis has shown that PutP binds proline with a Km of approximately 2 μM and sodium with a Km of approximately 700 μM . Sodium and proline are transported by PutP with a stoichiometry of 1:1 . The transport activity of PutP is associated with charge translocation . Sodium ions and/or proline induce a charge displacement and conformational alteration through the binding process at the cytoplasmic face of the protein...

## Biological Role

Catalyzes L-proline:Na+ symport (reaction.ecocyc.TRANS-RXN-118), TRANS-RXN0-505 (reaction.ecocyc.TRANS-RXN0-505). Transports L-Proline (molecule.C00148), Sodium cation (molecule.C01330).

## Annotation

FUNCTION: Catalyzes the sodium-dependent uptake of extracellular L-proline (PubMed:1567896, PubMed:3512540, PubMed:9693004). This protein is also capable of using lithium as the transport cation (PubMed:1567896, PubMed:9693004). Also catalyzes the uptake of propionate (PubMed:17088549). {ECO:0000269|PubMed:1567896, ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:3512540, ECO:0000269|PubMed:9693004}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-118|reaction.ecocyc.TRANS-RXN-118]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-505|reaction.ecocyc.TRANS-RXN0-505]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1015|gene.b1015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07117`
- `KEGG:ecj:JW1001;eco:b1015;ecoc:C3026_06175;`
- `GeneID:945602;`
- `GO:GO:0005298; GO:0005886; GO:0015193; GO:0015824; GO:0015912; GO:0031402; GO:0055085`

## Notes

Sodium/proline symporter (Proline carrier) (Proline permease) (Propionate transporter)
