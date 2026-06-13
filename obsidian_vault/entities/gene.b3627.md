---
entity_id: "gene.b3627"
entity_type: "gene"
name: "waaO"
source_database: "NCBI RefSeq"
source_id: "gene-b3627"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3627"
  - "waaO"
---

# waaO

`gene.b3627`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3627`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaO (gene.b3627) is a gene entity. It encodes waaO (protein.P27128). Encoded protein function: FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701, PubMed:9765561). Catalyzes the addition of a second glucose (glucose II) to the first outer-core glucose (glucose I) (PubMed:24479701, PubMed:9765561). In vitro, can add multiple glucose residues to its lipid acceptor (PubMed:24479701). Activity does not require the branched galactose added by WaaB, but it is higher in the presence of this branched galactose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-glucose, but not UDP-galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701, ECO:0000269|PubMed:9765561}. EcoCyc product frame: EG11352-MONOMER. EcoCyc synonyms: waaI, rfaI. Genomic coordinates: 3802039-3803058. EcoCyc protein note: The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . WaaO is a nonprocessive α-1,3 glucosyltransferase involved in the synthesis of the R core of lipopolysaccharide . WaaO adds the second glucose (GlcII) to the first glucose (GlcI) of the outer core of LPS . Activity of WaaO requires a functional waaB gene . Note that the E...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27128|protein.P27128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011860,ECOCYC:EG11352,GeneID:948143`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3802039-3803058:-; feature_type=gene
