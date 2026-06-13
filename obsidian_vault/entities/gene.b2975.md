---
entity_id: "gene.b2975"
entity_type: "gene"
name: "glcA"
source_database: "NCBI RefSeq"
source_id: "gene-b2975"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2975"
  - "glcA"
---

# glcA

`gene.b2975`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2975`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glcA (gene.b2975) is a gene entity. It encodes glcA (protein.Q46839). Encoded protein function: FUNCTION: Uptake of glycolate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport L-lactate and D-lactate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}. EcoCyc product frame: B2975-MONOMER. EcoCyc synonyms: yghK. Genomic coordinates: 3119597-3121279. EcoCyc protein note: GlcA (formerly YghK), is a glycolate transporter that belongs to the Lactate Permease Family (LctP) , due to its strong sequence similarity with the L-lactate permease, LCTP-MONOMER "LldP". GlcA transports the 2-hydroxymonocarboxylates, glycolate and L- and D-lactate . The glcA gene is located downstream from the glcDEFGB encoding the glycolate degradating enzymes malate synthase and glycolate oxidase. Expression studies using Northern blot analysis and lacZ fusion experiments have shown that the glcA gene is transcribed from the same promoter as the other glc structural genes . Expression of this operon is induced by growth on glycolate and is under the control of the transcriptional regulator, G7546-MONOMER "GlcC"...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lrp (protein.P0ACJ0), pdhR (protein.P0ACL9). Activated by lrp (protein.P0ACJ0), glcC (protein.P0ACL5), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46839|protein.Q46839]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACL5|protein.P0ACL5]] `RegulonDB` `S` - regulator=GlcC; target=glcA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=glcA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=glcA; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=glcA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009763,ECOCYC:G7542,GeneID:947259`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3119597-3121279:-; feature_type=gene
