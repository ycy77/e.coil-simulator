---
entity_id: "gene.b3702"
entity_type: "gene"
name: "dnaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3702"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3702"
  - "dnaA"
---

# dnaA

`gene.b3702`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3702`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaA (gene.b3702) is a gene entity. It encodes dnaA (protein.P03004). Encoded protein function: FUNCTION: Plays an essential in the initiation and regulation of chromosomal replication. Binds in an ATP-dependent fashion to the origin of replication (oriC) to initiate formation of the DNA replication initiation complex once per cell cycle (PubMed:3036372). Binds the DnaA box (consensus sequence 5'-TTATC[CA]A[CA]A-3') and separates the double-stranded (ds)DNA (PubMed:3036372, PubMed:18216012). Forms a right-handed helical filament on oriC DNA; dsDNA binds to the exterior of the filament while single-stranded (ss)DNA is stabiized in the filament's interior (By similarity). The ATP-DnaA-oriC complex binds and stabilizes the upper strand of the AT-rich DNA unwinding element (DUE) (PubMed:18216012). Mutagenesis of residues that line the central pore blocks dsDNA strand separation (PubMed:18216012). Subsequent binding of DNA polymerase III subunits leads to replisome formation (PubMed:3036372, PubMed:18216012). The DnaA-ATP form converts to DnaA-ADP; once converted to ADP the protein cannot initiate replication, ensuring only 1 round of replication per cell cycle (PubMed:3036372)...

## Biological Role

Repressed by dnaA (protein.P03004), fis (protein.P0A6R3), qseB (protein.P52076), nac (protein.Q47005). Activated by rpoD (protein.P00579), dnaA (protein.P03004), argP (protein.P0A8S1).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03004|protein.P03004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dnaA; function=+
- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=dnaA; function=-+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=dnaA; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=dnaA; function=-+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=dnaA; function=-
- `represses` <-- [[protein.P52076|protein.P52076]] `RegulonDB|EcoCyc` `S` - regulator=QseB; target=dnaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dnaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012103,ECOCYC:EG10235,GeneID:948217`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3882326-3883729:-; feature_type=gene
