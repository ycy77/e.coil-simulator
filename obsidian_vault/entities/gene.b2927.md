---
entity_id: "gene.b2927"
entity_type: "gene"
name: "epd"
source_database: "NCBI RefSeq"
source_id: "gene-b2927"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2927"
  - "epd"
---

# epd

`gene.b2927`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2927`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

epd (gene.b2927) is a gene entity. It encodes epd (protein.P0A9B6). Encoded protein function: FUNCTION: Catalyzes the NAD-dependent conversion of D-erythrose 4-phosphate to 4-phosphoerythronate. {ECO:0000269|PubMed:9182530, ECO:0000269|PubMed:9696782}. EcoCyc product frame: ERYTH4PDEHYDROG-MONOMER. EcoCyc synonyms: gapB, gap2. Genomic coordinates: 3072672-3073691. EcoCyc protein note: A tetrameric D-erythrose-4-phosphate dehydrogenase encoded by the epd gene in E. coli catalyses the first reaction of NAD-dependent oxidation of D-erythrose-4-phosphate in the de novo pyridoxine 5'-phosphate (vitamin B6) and pyridoxal 5'-phosphate biosynthesis. This enzyme shows an efficient non-phosphorylating erythrose 4-phosphate dehydrogenase activity and a low phosphorylating glyceraldehyde 3-phosphate dehydrogenase activity . Most of the amino acids that are essential for the chemical mechanism and for the binding of substrates and cofactors of the enzyme encoded by epd is conserved for its glycolytic enzyme GAPDH-A-MONOMER activity . There is a common chemical mechanism for the oxidation of glyceraldehyde 3-phosphate and erythrose 4-phosphate catalyzed by Epd. The reactions proceed through a two-step mechanism involving a covalent thioacyl intermediate with Cys-149. The limiting step is associated with the formation of this thioacyl intermediate...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9B6|protein.P0A9B6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=epd; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=epd; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=epd; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=epd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009607,ECOCYC:EG10368,GeneID:947413`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3072672-3073691:-; feature_type=gene
