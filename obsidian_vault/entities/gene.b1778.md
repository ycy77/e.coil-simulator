---
entity_id: "gene.b1778"
entity_type: "gene"
name: "msrB"
source_database: "NCBI RefSeq"
source_id: "gene-b1778"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1778"
  - "msrB"
---

# msrB

`gene.b1778`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1778`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msrB (gene.b1778) is a gene entity. It encodes msrB (protein.P0A746). Encoded protein function: Peptide methionine sulfoxide reductase MsrB (EC 1.8.4.12) (Peptide-methionine (R)-S-oxide reductase) EcoCyc product frame: EG12394-MONOMER. EcoCyc synonyms: yeaA. Genomic coordinates: 1862016-1862429. EcoCyc protein note: MsrB is one of several methionine sulfoxide reductases in E. coli . Methionine residues in proteins can be damaged by oxidation and can be repaired by methionine sulfoxide reductases . Modification of chemically oxidized N-terminal methionines by formylation or acetylation significantly increases the catalytic efficiency of reduction by MsrB and EG11433-MONOMER MsrA in redox kinetic studies in vitro . MsrA and MsrB are also important for keeping EG10823-MONOMER RecA active under oxidative stress conditions . Conversely, the transcription factor G7924 HypT is activated by methionine oxidation and inactivated by MsrA/MsrB activity . The CXXC motifs in MsrB are essential for metal binding and catalytic activity . Some organisms produce a methionine sulfoxide reductase composed of two domains with similarity to MsrA and MsrB, respectively, whereas E. coli produces these two distinct polypeptides. MsrB exhibits 1000-fold lower catalytic efficiency than MsrA toward free methionine sulfoxide...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by Cra-β-D-fructofuranose 1-phosphate (complex.ecocyc.CPLX-127), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A746|protein.P0A746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX-127|complex.ecocyc.CPLX-127]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=msrB; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=msrB; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=msrB; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=msrB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005916,ECOCYC:EG12394,GeneID:947188`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1862016-1862429:-; feature_type=gene
