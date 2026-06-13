---
entity_id: "gene.b3904"
entity_type: "gene"
name: "rhaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3904"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3904"
  - "rhaB"
---

# rhaB

`gene.b3904`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3904`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaB (gene.b3904) is a gene entity. It encodes rhaB (protein.P32171). Encoded protein function: FUNCTION: Involved in the catabolism of L-rhamnose (6-deoxy-L-mannose). It could also play a role in the metabolism of some rare sugars such as L-fructose. Catalyzes the transfer of the gamma-phosphate group from ATP to the 1-hydroxyl group of L-rhamnulose to yield L-rhamnulose 1-phosphate. Uridine triphosphate (UTP), cytidine 5-triphosphate (CTP), guanosine 5-triphosphate (GTP), and thymidine triphosphate (TTP) also can act as phosphoryl donors. It can also phosphorylate L-fuculose and L-xylulose. {ECO:0000255|HAMAP-Rule:MF_01535, ECO:0000269|PubMed:14264882, ECO:0000269|PubMed:16674975, ECO:0000269|PubMed:5341476}. EcoCyc product frame: RHAMNULOKIN-MONOMER. Genomic coordinates: 4095979-4097448. EcoCyc protein note: L-rhamnulose kinase catalyzes the second step of rhamnose degradation, the phosphorylation of rhamnulose. The substrate spectrum of L-rhamnulose kinase has been investigated; the enzyme shows a broad tolerance for structural modifications of the natural substrate . Rare sugars have been modeled into the active center of the crystal structure . L-rhamnulose kinase is a monomer in solution...

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32171|protein.P32171]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaB; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `C` - regulator=RhaS; target=rhaB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rhaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012738,ECOCYC:EG11868,GeneID:948399`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4095979-4097448:-; feature_type=gene
