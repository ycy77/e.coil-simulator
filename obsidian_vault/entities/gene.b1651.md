---
entity_id: "gene.b1651"
entity_type: "gene"
name: "gloA"
source_database: "NCBI RefSeq"
source_id: "gene-b1651"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1651"
  - "gloA"
---

# gloA

`gene.b1651`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1651`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gloA (gene.b1651) is a gene entity. It encodes gloA (protein.P0AC81). Encoded protein function: FUNCTION: Catalyzes the isomerization of the hemithioacetal formed spontaneously from methylglyoxal and glutathione, to S-lactoylglutathione, which is then hydrolyzed by a type II glyoxalase (GloB or GloC). Is involved in methylglyoxal (MG) detoxification (Probable) (PubMed:10913283). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). {ECO:0000269|PubMed:10913283, ECO:0000269|PubMed:23536188, ECO:0000305|PubMed:25670698}. EcoCyc product frame: GLYOXI-MONOMER. Genomic coordinates: 1727837-1728244. EcoCyc protein note: Glyoxalase I catalyzes the first of two sequential steps in the conversion of methylgloxal to D-lactate. The enzyme tightly binds one ion of nickel per enzyme dimer and is the first example of a nickel-containing glyoxalase . Glyoxalase I shows lower levels of activity with a number of other metal ion cofactors including Co2+, but not including Zn2+ . Crystal structures of glyoxalase I in the apo form and in complex with various metal ions have been determined . The nickel active site structure has been probed by X-ray absorption studies . The two active sites of the homodimer are initially asymmetric; only one site binds Ni2+...

## Biological Role

Repressed by rutR (protein.P0ACU2), nemR (protein.P67430).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC81|protein.P0AC81]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=gloA; function=-
- `represses` <-- [[protein.P67430|protein.P67430]] `RegulonDB` `S` - regulator=NemR; target=gloA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005520,ECOCYC:G6891,GeneID:946161`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1727837-1728244:+; feature_type=gene
