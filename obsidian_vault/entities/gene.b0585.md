---
entity_id: "gene.b0585"
entity_type: "gene"
name: "fes"
source_database: "NCBI RefSeq"
source_id: "gene-b0585"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0585"
  - "fes"
---

# fes

`gene.b0585`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0585`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fes (gene.b0585) is a gene entity. It encodes fes (protein.P13039). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of ferric enterobactin (Fe-Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Is responsible for the release of iron from ferric enterobactin (PubMed:1534808). Also catalyzes the hydrolysis of iron-free enterobactin (Ent) (PubMed:150859, PubMed:1534808, PubMed:8148617). Cleavage of ferric enterobactin results in a mixture of three hydrolysis products, 2,3-dihydroxybenzoylserine (DHBS), the linear dimer (DHBS)2 and the linear trimer (DHBS)3, while cleavage of iron-free enterobactin yields only the monomer (PubMed:8148617). Hydrolysis of ferric enterobactin is less efficient than hydrolysis of unliganded enterobactin (PubMed:150859, PubMed:1534808). It also cleaves the aluminum (III) complex at a rate similar to the ferric complex (PubMed:1534808). {ECO:0000269|PubMed:150859, ECO:0000269|PubMed:1534808, ECO:0000269|PubMed:8148617}. EcoCyc product frame: EG10299-MONOMER. Genomic coordinates: 612737-613939. EcoCyc protein note: Enterochelin (enterobactin, Ent) esterase (Fes) catalyzes the hydrolysis of both enterobactin and ferric enterobactin. The enzyme produces the linear 2,3-dihydroxy-N-benzoyl-L-serine trimer as well as the dimer and monomer . Hydrolysis of ferric enterobactin is less efficient than hydrolysis of unliganded enterobactin...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13039|protein.P13039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fes; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=fes; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fes; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002019,ECOCYC:EG10299,GeneID:945181`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:612737-613939:+; feature_type=gene
