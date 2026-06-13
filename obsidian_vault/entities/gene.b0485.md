---
entity_id: "gene.b0485"
entity_type: "gene"
name: "glsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0485"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0485"
  - "glsA"
---

# glsA

`gene.b0485`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0485`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glsA (gene.b0485) is a gene entity. It encodes glsA1 (protein.P77454). Encoded protein function: Glutaminase 1 (EC 3.5.1.2) EcoCyc product frame: G6261-MONOMER. EcoCyc synonyms: ybaS. Genomic coordinates: 511641-512573. EcoCyc protein note: GlsA (YbaS) is a glutaminase that is highly selective for L-glutamine. Based on the pH profile of the enzymatic activity, GlsA was proposed to correspond to the previously described GLUTAMINA-CPLX of E. coli B. Glutamine binding exhibits positive cooperativity . Together with the antiporter XASA-MONOMER GadC, GlsA constitutes an acid resistance system. GlsA. which is activated by acidic conditions, converts GLN to GLT and neutralizes H+ by producing ammonia, which binds a proton to form ammonium . A crystal structure of unliganded GlsA has been solved at 1.6 Å resolution; an active site has been predicted, and site-directed mutagenesis confirmed the importance of various conserved residues for catalytic activity. The S66 residue is proposed to act as a catalytic nucleophile, and the enzyme is predicted to employ a β-lactamase-like catalytic mechanism . Under certain growth conditions, a glsA deletion mutant shows a reduced growth rate . glsA is required for glutamine-mediated acid resistance . Expression of glsA is increased during acid shock . glsA is associated with isobutanol tolerance in an engineered E. coli strain . Review:

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by rpoS (protein.P13445), gadX (protein.P37639).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77454|protein.P77454]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glsA; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=glsA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001688,ECOCYC:G6261,GeneID:946187`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:511641-512573:+; feature_type=gene
