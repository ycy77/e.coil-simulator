---
entity_id: "gene.b2040"
entity_type: "gene"
name: "rfbD"
source_database: "NCBI RefSeq"
source_id: "gene-b2040"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2040"
  - "rfbD"
---

# rfbD

`gene.b2040`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2040`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfbD (gene.b2040) is a gene entity. It encodes rfbD (protein.P37760). Encoded protein function: FUNCTION: Involved in the biosynthesis of the dTDP-L-rhamnose which is an important component of lipopolysaccharide (LPS) (Probable). Catalyzes the reduction of dTDP-6-deoxy-L-lyxo-4-hexulose to yield dTDP-L-rhamnose (By similarity). RmlD uses NADH and NADPH nearly equally well (By similarity). {ECO:0000250|UniProtKB:P26392, ECO:0000305|PubMed:7517391}. EcoCyc product frame: DTDPDEHYRHAMREDUCT-MONOMER. EcoCyc synonyms: rmlD. Genomic coordinates: 2111077-2111976. EcoCyc protein note: dTDP-4-dehydrorhamnose reductase (RfbD) is the final enzyme of the DTDPRHAMSYN-PWY pathway, which synthesizes one of the precursors for the O antigen of lipopolysaccharide. RfbD catalyzes the stereospecific reduction of the 4-keto group of dTDP-4-dehydro-6-deoxy-L-mannose to generate the final product, dTDP-L-rhamnose. The E. coli enzyme has not been biochemically characterized. E. coli K-12 strains carry mutations in the rfb gene cluster and do not produce O antigen. In MG1655, the rfb-50 allele, an IS5 insertion, interrupts the wbbL gene, which would encode the dTDP-rhamnose transferase . Deletion of rfbD enables increased production of quercetin 3-O-(6-deoxytalose) in an engineered E. coli strain . dTDP-4-dehydrorhamnose reductase has primarily been investigated in Salmonella enterica...

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37760|protein.P37760]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006764,ECOCYC:EG12411,GeneID:947117`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2111077-2111976:-; feature_type=gene
