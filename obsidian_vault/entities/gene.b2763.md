---
entity_id: "gene.b2763"
entity_type: "gene"
name: "cysI"
source_database: "NCBI RefSeq"
source_id: "gene-b2763"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2763"
  - "cysI"
---

# cysI

`gene.b2763`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2763`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysI (gene.b2763) is a gene entity. It encodes cysI (protein.P17846). Encoded protein function: FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. {ECO:0000255|HAMAP-Rule:MF_01540}. EcoCyc product frame: BETACOMP-MONOMER. Genomic coordinates: 2888387-2890099. EcoCyc protein note: CysI is the β or hemoprotein subunit (SiRHP) of sulfite reductase (SiR). Sulfite reductase is involved in the assimilation of sulfate and catalyzes the transfer of six electrons from NADPH to sulfite to produce sulfide. CysI contains one siroheme and one [4Fe-4S] cluster per polypeptide; it transfers the electrons through the [4Fe-4S] cluster to the siroheme . The heme and iron-sulfur cluster are exchange-coupled . Experiments with the enzyme purified from E. coli B showed that the isolated, monomeric hemoprotein is able to catalyze sulfite reduction at a reduced rate using an artificial electron donor, but not NADPH . Crystal structures of CysI have been solved .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17846|protein.P17846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009061,ECOCYC:EG10190,GeneID:947231`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2888387-2890099:-; feature_type=gene
