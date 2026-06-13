---
entity_id: "gene.b1473"
entity_type: "gene"
name: "yddG"
source_database: "NCBI RefSeq"
source_id: "gene-b1473"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1473"
  - "yddG"
---

# yddG

`gene.b1473`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1473`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yddG (gene.b1473) is a gene entity. It encodes yddG (protein.P46136). Encoded protein function: FUNCTION: Amino acid transporter with broad substrate specificity (PubMed:17784858, PubMed:27281193). Can transport various amino acids, including phenylalanine, tyrosine, tryptophan, L-threonine, L-methionine, L-lysine, L-glutamate, L-valine and L-isoleucine (PubMed:17784858, PubMed:27281193). Overexpression confers resistance to phenylalanine and increases export of phenylalanine, tyrosine and tryptophan (PubMed:17784858). {ECO:0000269|PubMed:17784858, ECO:0000269|PubMed:27281193}. EcoCyc product frame: EG12713-MONOMER. Genomic coordinates: 1546288-1547169. EcoCyc protein note: YddG is an amino acid exporter with broad specificity. YddG is a member of the Aromatic Amino Acid/Paraquat Exporter (ArAA/P-E) Family (TC: 2.A.7.17) within the Drug/Metabolite Transporter (DMT) superfamily . YddG is predicted to be an inner membrane protein with nine or ten transmembrane domains; experimental topology analysis supports a model of 10 transmembrane helices with the N and C-termini located in the cytoplasm Expression of yddG from a multicopy plasmid results in increased resistance to phenylalanine, and to the aromatic amino acid analogues DL-p-fluorophenylalanine, DL-o-fluorophenylalanine, and 5-fluorotryptophane . Overexpression of yddG in E...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46136|protein.P46136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yddG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004912,ECOCYC:EG12713,GeneID:945942`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1546288-1547169:-; feature_type=gene
