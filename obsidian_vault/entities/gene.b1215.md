---
entity_id: "gene.b1215"
entity_type: "gene"
name: "kdsA"
source_database: "NCBI RefSeq"
source_id: "gene-b1215"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1215"
  - "kdsA"
---

# kdsA

`gene.b1215`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1215`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdsA (gene.b1215) is a gene entity. It encodes kdsA (protein.P0A715). Encoded protein function: FUNCTION: Synthesis of KDO 8-P which is required for lipid A maturation and cellular growth. EcoCyc product frame: KDO-8PSYNTH-MONOMER. Genomic coordinates: 1268165-1269019. EcoCyc protein note: 3-deoxy-D-manno-octulosonate 8-phosphate (KDO-8-P) synthase is a key enzyme in lipopolysaccharide biosynthesis. It catalyzes the condensation of arabinose-5-phosphate and PEP by cleavage of the C-O bond in PEP, forming the eight-carbon skeleton of 3-deoxy-D-manno-octulosonate, which serves as a linker between the hydrophobic portion of lipopolysaccharide, lipid A, and the hydrophilic polysaccharide chain. The reaction mechanism has been studied extensively . Various crystal structures of KdsA have been solved . The enzyme appears to be a homotetramer , although initial biochemical data of the E. coli B enzyme seemed to favor a trimeric form . The crystal structures allowed confirmation of the observed stereochemical preferences and reaction mechanism of the enzyme and provide an explanation for the irreversible nature of the reaction . Two cysteine residues, C38 and C166, are important for catalytic activity . Two conserved histidine residues, H97 and H241, are important for catalytic activity, and a third residue, H202, is essential . The wild type E...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), glaR (protein.P37338).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A715|protein.P0A715]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdsA; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=kdsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=kdsA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004077,ECOCYC:EG10518,GeneID:945785`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1268165-1269019:+; feature_type=gene
