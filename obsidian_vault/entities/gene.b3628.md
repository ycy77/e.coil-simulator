---
entity_id: "gene.b3628"
entity_type: "gene"
name: "waaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3628"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3628"
  - "waaB"
---

# waaB

`gene.b3628`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3628`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaB (gene.b3628) is a gene entity. It encodes waaB (protein.P27127). Encoded protein function: FUNCTION: Galactosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:24479701). Catalyzes the addition of galactose from UDP-galactose to the first glucose residue of the LPS outer core (PubMed:24479701). Cannot use other sugar donors, such as UDP-glucose, UDP-glucuronic acid, UDP-galacuronic acid, GDP-mannose, ADP-glucose and GDP-glucose (PubMed:24479701). In the absence of a lipid acceptor, can hydrolyze UDP-galactose to UDP and galactose (PubMed:24479701). {ECO:0000269|PubMed:24479701}. EcoCyc product frame: EG11351-MONOMER. EcoCyc synonyms: lps, syn, rfaB. Genomic coordinates: 3803058-3804137. EcoCyc protein note: The lipopolysaccharide (LPS) of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . UDP-galactose:(glucosyl)lipopolysaccharide 1,6-D-galactosyltransferase (WaaB) adds galactose from UDP-galactose to the first glucose residue (GlcI) of the outer core of LPS . Early studies characterized the waa (rfa) locus and identified the waaB gene . In the absence of the lipid acceptor, WaaB can slowly hydrolyze the UDP-galactose sugar donor. It cannot hydrolyze UDP-glucose...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27127|protein.P27127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011862,ECOCYC:EG11351,GeneID:948144`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3803058-3804137:-; feature_type=gene
