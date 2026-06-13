---
entity_id: "gene.b4040"
entity_type: "gene"
name: "ubiA"
source_database: "NCBI RefSeq"
source_id: "gene-b4040"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4040"
  - "ubiA"
---

# ubiA

`gene.b4040`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4040`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiA (gene.b4040) is a gene entity. It encodes ubiA (protein.P0AGK1). Encoded protein function: FUNCTION: Catalyzes the prenylation of para-hydroxybenzoate (PHB) with an all-trans polyprenyl group. Mediates the second step in the final reaction sequence of ubiquinone-8 (UQ-8) biosynthesis, which is the condensation of the polyisoprenoid side chain with PHB, generating the first membrane-bound Q intermediate 3-octaprenyl-4-hydroxybenzoate (PubMed:4552989). Geranyldiphosphate (GPP), all-trans-farnesyldiphosphate (FPP) and all-trans-solanesyldiphosphate (SPP) are also accepted as side chain precursors (PubMed:8155731). {ECO:0000269|PubMed:4552989, ECO:0000269|PubMed:8155731}. EcoCyc product frame: 4OHBENZOATE-OCTAPRENYLTRANSFER-MONOMER. EcoCyc synonyms: cyr. Genomic coordinates: 4253016-4253888. EcoCyc protein note: 4-Hydroxybenzoate octaprenyltransferase is the second enzyme in the pathway of ubiquinone biosynthesis. It is responsible for the prenylation of 4-hydroxybenzoate using a polyprenyldiphosphate as a side chain precursor. While E. coli produces an octapreny diphosphatel natively, UbiA is not specific to that compound and can accept polyprenyl diphosphates of different lengths . UbiA is an inner membrane protein with seven predicted transmembrane domains. The C terminus is located in the periplasm . Earlier work experimentally localized UbiA to the membrane fraction...

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGK1|protein.P0AGK1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ubiA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013229,ECOCYC:EG11370,GeneID:948540`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4253016-4253888:+; feature_type=gene
