---
entity_id: "gene.b1852"
entity_type: "gene"
name: "zwf"
source_database: "NCBI RefSeq"
source_id: "gene-b1852"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1852"
  - "zwf"
---

# zwf

`gene.b1852`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1852`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zwf (gene.b1852) is a gene entity. It encodes zwf (protein.P0AC53). Encoded protein function: FUNCTION: Catalyzes the oxidation of glucose 6-phosphate to 6-phosphogluconolactone. {ECO:0000255|HAMAP-Rule:MF_00966, ECO:0000269|PubMed:15113569, ECO:0000269|PubMed:17962566}.; FUNCTION: Probable source of extracellular death factor (EDF, sequence Asn-Asn-Trp-Asn-Asn, NNWNN) following processing and amidation. This pentapeptide stimulates cell death mediated by MazF (PubMed:17962566). Artificial peptides with altered sequence show that NNGNN, GNWNG and NWN no longer stimulate MazF's endoribonuclease activity; other peptides (NNGN, GNWMM, NNWNG, NNNWNNN) retain MazF-stimulating activity. NNWNN, NNGN, GNWMM and NNWNG prevent cognate antitoxin MazE from inhibiting MazF; although NNNWNNN stimulates MazF it does not do so in the presence of MazE. EDF also stimulates ChpB's endoribonuclease activity in vitro; in this case NWN partially stimulates ChpB, whereas NNGNN, GNWNN, NNWNG, GNWNG and NNNWNNN do not. Only the wild-type EDF peptide prevents cognate antitoxin ChpS from inhibiting ChpB (PubMed:21419338). {ECO:0000269|PubMed:17962566, ECO:0000269|PubMed:21419338}. EcoCyc product frame: GLU6PDEHYDROG-MONOMER. Genomic coordinates: 1934839-1936314...

## Biological Role

Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC53|protein.P0AC53]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=zwf; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=zwf; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=zwf; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006171,ECOCYC:EG11221,GeneID:946370`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1934839-1936314:-; feature_type=gene
