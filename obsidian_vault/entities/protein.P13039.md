---
entity_id: "protein.P13039"
entity_type: "protein"
name: "fes"
source_database: "UniProt"
source_id: "P13039"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:1534808}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fes b0585 JW0576"
---

# fes

`protein.P13039`

## Static

- Type: `protein`
- Source: `UniProt:P13039`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:1534808}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of ferric enterobactin (Fe-Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Is responsible for the release of iron from ferric enterobactin (PubMed:1534808). Also catalyzes the hydrolysis of iron-free enterobactin (Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Cleavage of ferric enterobactin results in a mixture of three hydrolysis products, 2,3-dihydroxybenzoylserine (DHBS), the linear dimer (DHBS)2 and the linear trimer (DHBS)3, while cleavage of iron-free enterobactin yields only the monomer (PubMed:8148617). Hydrolysis of ferric enterobactin is less efficient than hydrolysis of unliganded enterobactin (PubMed:150859, PubMed:1534808). It also cleaves the aluminum (III) complex at a rate similar to the ferric complex (PubMed:1534808). {ECO:0000269|PubMed:150859, ECO:0000269|PubMed:1534808, ECO:0000269|PubMed:8148617}. Enterochelin (enterobactin, Ent) esterase (Fes) catalyzes the hydrolysis of both enterobactin and ferric enterobactin. The enzyme produces the linear 2,3-dihydroxy-N-benzoyl-L-serine trimer as well as the dimer and monomer . Hydrolysis of ferric enterobactin is less efficient than hydrolysis of unliganded enterobactin . The catalytic activity of the Fes ortholog in E...

## Biological Role

Catalyzes RXN-20025 (reaction.ecocyc.RXN-20025), enterobactin hydrolase (reaction.ecocyc.RXN0-1661), RXN0-6938 (reaction.ecocyc.RXN0-6938).

## Annotation

FUNCTION: Catalyzes the hydrolysis of ferric enterobactin (Fe-Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Is responsible for the release of iron from ferric enterobactin (PubMed:1534808). Also catalyzes the hydrolysis of iron-free enterobactin (Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Cleavage of ferric enterobactin results in a mixture of three hydrolysis products, 2,3-dihydroxybenzoylserine (DHBS), the linear dimer (DHBS)2 and the linear trimer (DHBS)3, while cleavage of iron-free enterobactin yields only the monomer (PubMed:8148617). Hydrolysis of ferric enterobactin is less efficient than hydrolysis of unliganded enterobactin (PubMed:150859, PubMed:1534808). It also cleaves the aluminum (III) complex at a rate similar to the ferric complex (PubMed:1534808). {ECO:0000269|PubMed:150859, ECO:0000269|PubMed:1534808, ECO:0000269|PubMed:8148617}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-20025|reaction.ecocyc.RXN-20025]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1661|reaction.ecocyc.RXN0-1661]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6938|reaction.ecocyc.RXN0-6938]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0585|gene.b0585]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13039`
- `KEGG:ecj:JW0576;eco:b0585;ecoc:C3026_02915;`
- `GeneID:945181;`
- `GO:GO:0005506; GO:0005737; GO:0008849; GO:0033214; GO:0046214`
- `EC:3.1.1.108`

## Notes

Iron(III) enterobactin esterase (EC 3.1.1.108) (Enterochelin esterase) (Ferric enterobactin esterase)
