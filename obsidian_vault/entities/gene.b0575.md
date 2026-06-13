---
entity_id: "gene.b0575"
entity_type: "gene"
name: "cusA"
source_database: "NCBI RefSeq"
source_id: "gene-b0575"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0575"
  - "cusA"
---

# cusA

`gene.b0575`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0575`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusA (gene.b0575) is a gene entity. It encodes cusA (protein.P38054). Encoded protein function: FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}. EcoCyc product frame: YBDE-MONOMER. EcoCyc synonyms: ybdE. Genomic coordinates: 598714-601857. EcoCyc protein note: CusA is a member of the Resistance-Nodulation-Cell Division (RND) Transporter Superfamily and is involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusA contains 12 transmembrane (TM) segments and a large periplasmic domain formed from two loops located between TM1 and 2 and TM7 and 8 . As an RND transporter, CusA probably forms trimers in vivo, but it forms a mixture of oligomers in detergent solution . The amino acids M573, M623, M672, D405, E412, and A399 of CusA are essential for copper tolerance . Crystal structures of apo and ion bound CusA suggest that the protein uses methionine pairs or clusters to export copper and silver ions from both the cytoplasm and the periplasm. 3 methionine residues - M573, M623 and M672 coordinate Cu(I) bound in a periplasmic cleft...

## Biological Role

Repressed by yieP (protein.P31475). Activated by rpoD (protein.P00579), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38054|protein.P38054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusA; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusA; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusA; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusA; function=+
- `represses` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001971,ECOCYC:EG12367,GeneID:945191`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:598714-601857:+; feature_type=gene
