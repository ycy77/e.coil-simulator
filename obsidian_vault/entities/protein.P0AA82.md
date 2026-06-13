---
entity_id: "protein.P0AA82"
entity_type: "protein"
name: "codB"
source_database: "UniProt"
source_id: "P0AA82"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "codB b0336 JW0327"
---

# codB

`protein.P0AA82`

## Static

- Type: `protein`
- Source: `UniProt:P0AA82`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for cytosine transport into the cell. CodB is a cytosine transporter which probably functions as a cytosine/proton symporter. Whole cell transport assays have shown that the cloned codB gene can complement mutants with cytosine transport defects which had mapped to a locus near the codA gene . The codB gene is located in a cytosine-inducible operon with the codA gene encoding cytosine deaminase . Consistent with this, CodB belongs to the NCS1 family of purine and pyrimidine transporters . Analysis of alkaline phosphatase and β-galactosidase fusions has suggested that CodB consists of twelve TMS . Imported cytosine can be metabolised via hydrolytic deamination by CodA to yield uracil and ammonia.

## Biological Role

Catalyzes cytosine:proton symport (reaction.ecocyc.TRANS-RXN-116). Transports Cytosine (molecule.C00380), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Required for cytosine transport into the cell.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-116|reaction.ecocyc.TRANS-RXN-116]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0336|gene.b0336]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA82`
- `KEGG:ecj:JW0327;eco:b0336;ecoc:C3026_01645;ecoc:C3026_24815;`
- `GeneID:944994;`
- `GO:GO:0005886; GO:0015209; GO:0015856; GO:0016020; GO:0019858; GO:1902600`

## Notes

Cytosine permease
