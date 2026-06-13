---
entity_id: "gene.b3619"
entity_type: "gene"
name: "rfaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3619"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3619"
  - "rfaD"
---

# rfaD

`gene.b3619`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3619`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfaD (gene.b3619) is a gene entity. It encodes hldD (protein.P67910). Encoded protein function: FUNCTION: Catalyzes the interconversion between ADP-D-glycero-beta-D-manno-heptose and ADP-L-glycero-beta-D-manno-heptose via an epimerization at carbon 6 of the heptose. {ECO:0000269|PubMed:6337148, ECO:0000269|PubMed:7929099}. EcoCyc product frame: EG10838-MONOMER. EcoCyc synonyms: waaD, hldD, htrM, nbsB. Genomic coordinates: 3793987-3794919. EcoCyc protein note: The rfaD gene encodes ADP-L-glycero-D-mannoheptose-6-epimerase, the last enzyme in the pathway for synthesis of the ADP-heptose precursor of core LPS . The enzyme is glycosylated . It was initially thought to contain NAD+ as a cofactor , but the cofactor found in the crystal structure was NADP+ . Subsequent studies showed that the enzyme has a preference of NADP+ over NAD+ . A crystal structure of RfaD has been solved at 2 Å resolution . The enzyme was initially thought to form a homohexamer , but appears as a homopentamer in the crystal structure . A reaction mechanism involving transient oxidation of the C-6'' stereocenter of the substrate and transient reduction of the NADP+ cofactor has been proposed . Catalysis involves two basic residues, Tyr140 and Lys178 . Only very small amounts of the transiently oxidized 6''-keto intermediate are released from the enzyme during catalysis...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6), zraR (protein.P14375).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67910|protein.P67910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rfaD; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=rfaD; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rfaD; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=rfaD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011843,ECOCYC:EG10838,GeneID:948134`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3793987-3794919:+; feature_type=gene
