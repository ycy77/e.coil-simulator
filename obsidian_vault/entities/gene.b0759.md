---
entity_id: "gene.b0759"
entity_type: "gene"
name: "galE"
source_database: "NCBI RefSeq"
source_id: "gene-b0759"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0759"
  - "galE"
---

# galE

`gene.b0759`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0759`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galE (gene.b0759) is a gene entity. It encodes galE (protein.P09147). Encoded protein function: FUNCTION: Involved in the metabolism of galactose. Catalyzes the conversion of UDP-galactose (UDP-Gal) to UDP-glucose (UDP-Glc) through a mechanism involving the transient reduction of NAD. It is only active on UDP-galactose and UDP-glucose. {ECO:0000269|PubMed:14235524}. EcoCyc product frame: UDPGLUCEPIM-MONOMER. EcoCyc synonyms: galD. Genomic coordinates: 791039-792055. EcoCyc protein note: UDP-glucose 4-epimerase (GalE) catalyzes a hydride transfer in the interconversion of UDP-galactose and UDP-glucose as part of galactose catabolism. The active epimerase contains two molecules of NAD+ per dimer . The monomer may also be catalytically active . The reaction mechanism has been studied extensively. The reaction proceeds via an intermolecular hydrogen transfer . The bound NAD+ is transiently reduced in the course of the reaction and was thought to be accompanied by a change in protein structure . When uridine nucleotides bind to the substrate site, it was thought that a protein conformational change is induced which increases the chemical reactivity of NAD+ . Complexes of UDP-glucose 4-epimerase containing NADH and uridine nucleotide are inactive . A number of crystal structures of the enzyme with a variety of ligands have been solved...

## Biological Role

Repressed by galR (protein.P03024), hns (protein.P0ACF8), crp (protein.P0ACJ8), galS (protein.P25748). Activated by rpoD (protein.P00579), galR (protein.P03024), crp (protein.P0ACJ8), rpoS (protein.P13445), galS (protein.P25748).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09147|protein.P09147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=galE; function=+
- `activates` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galE; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galE; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=galE; function=+
- `activates` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galE; function=-+
- `represses` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galE; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=galE; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=galE; function=-+
- `represses` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `S` - regulator=GalS; target=galE; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002575,ECOCYC:EG10362,GeneID:945354`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:791039-792055:-; feature_type=gene
