---
entity_id: "gene.b3256"
entity_type: "gene"
name: "accC"
source_database: "NCBI RefSeq"
source_id: "gene-b3256"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3256"
  - "accC"
---

# accC

`gene.b3256`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3256`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

accC (gene.b3256) is a gene entity. It encodes accC (protein.P24182). Encoded protein function: FUNCTION: This protein is a component of the acetyl coenzyme A carboxylase complex; first, biotin carboxylase catalyzes the carboxylation of the carrier protein and then the transcarboxylase transfers the carboxyl group to form malonyl-CoA. {ECO:0000305|PubMed:16793549, ECO:0000305|PubMed:19213731}. EcoCyc product frame: BIOTIN-CARBOXYL-MONOMER. EcoCyc synonyms: fabG. Genomic coordinates: 3405917-3407266. EcoCyc protein note: Mutations in the homologous and functionally identical subunit in mammalian proprionyl-CoA carboxylase and 3-methylcrotonyl-CoA carboxylase result in the metabolic deficiency diseases of propionic acidemia or methylcrotonylglycinuria. Kinetic analysis of mutants analogous to the disease-causing mutants has been performed to determine the function of those residues . Studies with dimerization-deficient accC mutants showed that only dimeric biotin carboxylase fulfills its physiological function in vivo .

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24182|protein.P24182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=accC; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=accC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010677,ECOCYC:EG10276,GeneID:947761`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3405917-3407266:+; feature_type=gene
