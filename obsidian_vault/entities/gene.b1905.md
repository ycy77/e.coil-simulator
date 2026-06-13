---
entity_id: "gene.b1905"
entity_type: "gene"
name: "ftnA"
source_database: "NCBI RefSeq"
source_id: "gene-b1905"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1905"
  - "ftnA"
---

# ftnA

`gene.b1905`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1905`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftnA (gene.b1905) is a gene entity. It encodes ftnA (protein.P0A998). Encoded protein function: FUNCTION: Iron-storage protein. {ECO:0000269|PubMed:11254384}. EcoCyc product frame: EG10921-MONOMER. EcoCyc synonyms: ftn, gen-165, rsgA. Genomic coordinates: 1988716-1989213. EcoCyc protein note: ftnA encodes the iron-storage protein ferritin, which is similar to human ferritin H . Ferritin forms a multi-subunit, hollow spherical shell of 24 individual ferritin polypeptides that can sequester more than 2000 iron atoms in the center . Ferritin and CPLX0-1421 are distantly related . The crystal structure of ferritin has been determined, identifying three iron-binding sites per subunit . Two of these sites form a dinuclear iron center where oxidation of Fe(II) occurs, allowing iron to be stored as ferric phosphate . The third site appears to modulate Fe2+ binding to the dinuclear iron center . No protons are released upon initial binding of Fe2+. Subsequent oxidation of Fe2+ leads to production of H2O2, which is itself utilized for oxidation of Fe2+ bound at other ferroxidase centers . The iron core forms a hollow sphere in the presence of phosphate . In vitro, FtnA was shown to sequester iron released from damaged [2Fe-2S] clusters of IscU. Iron sequestered by FtnA can be transferred to IscA, but not IscU...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A998|protein.P0A998]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=ftnA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=ftnA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006342,ECOCYC:EG10921,GeneID:946410`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1988716-1989213:+; feature_type=gene
