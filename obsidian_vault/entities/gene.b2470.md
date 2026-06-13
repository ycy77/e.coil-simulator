---
entity_id: "gene.b2470"
entity_type: "gene"
name: "acrD"
source_database: "NCBI RefSeq"
source_id: "gene-b2470"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2470"
  - "acrD"
---

# acrD

`gene.b2470`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2470`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrD (gene.b2470) is a gene entity. It encodes acrD (protein.P24177). Encoded protein function: FUNCTION: Participates in the efflux of aminoglycosides. Confers resistance to a variety of these substances. {ECO:0000269|PubMed:10692383}. EcoCyc product frame: ACRD-MONOMER. EcoCyc synonyms: yffA. Genomic coordinates: 2587595-2590708. EcoCyc protein note: AcrD is a member of the resistance-nodulation-division (RND) superfamily and a component of the AcrAD-TolC efflux pump complex in E. coli K-12. AcrD is homologous to the major efflux pump permease AcrB . Disruption of acrD in the K-12 strain JC7623 increases susceptibility to a range of aminoglycoside antibiotics (amikacin, gentamicin, tobramycin, kanamycin and neomycin) and cells accumulate higher levels of labeled dihydrostreptomycin and gentamicin than the parent strain; disruption of acrD in the K-12 strain JC7623 slightly increases susceptibility to erythromycin and puromycin but does not affect susceptibility to a range of other compounds including crystal violet, novobiocin, rifampin, chloramphenicol, carbenicillin, cefoxitin, nalidixic acid, norfloxacin and ampicillin (see also )...

## Biological Role

Activated by cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24177|protein.P24177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=acrD; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=acrD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008136,ECOCYC:EG10014,GeneID:945464`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2587595-2590708:+; feature_type=gene
