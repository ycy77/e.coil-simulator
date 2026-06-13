---
entity_id: "gene.b0583"
entity_type: "gene"
name: "entD"
source_database: "NCBI RefSeq"
source_id: "gene-b0583"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0583"
  - "entD"
---

# entD

`gene.b0583`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0583`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entD (gene.b0583) is a gene entity. It encodes entD (protein.P19925). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. Plays an essential role in the assembly of the enterobactin by catalyzing the transfer of the 4'-phosphopantetheine (Ppant) moiety from coenzyme A to the apo-domains of both EntB (ArCP domain) and EntF (PCP domain) to yield their holo-forms which make them competent for the activation of 2,3-dihydroxybenzoate (DHB) and L-serine, respectively. {ECO:0000269|PubMed:8939709, ECO:0000269|PubMed:9214294, ECO:0000269|PubMed:9485415}. EcoCyc product frame: ENTD-MONOMER. Genomic coordinates: 609459-610079. EcoCyc protein note: AcpS is the founding member of a 4'-phosphopantetheinyl (P-pant) transferase protein family that includes E. coli EntD, E. coli o195 protein, and Bacillus subtilis Sfp; family members share two conserved motifs but relatively low sequence identity overall...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19925|protein.P19925]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=entD; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002009,ECOCYC:EG10262,GeneID:945194`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:609459-610079:-; feature_type=gene
