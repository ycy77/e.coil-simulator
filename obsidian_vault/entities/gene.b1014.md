---
entity_id: "gene.b1014"
entity_type: "gene"
name: "putA"
source_database: "NCBI RefSeq"
source_id: "gene-b1014"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1014"
  - "putA"
---

# putA

`gene.b1014`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1014`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

putA (gene.b1014) is a gene entity. It encodes putA (protein.P09546). Encoded protein function: FUNCTION: Oxidizes proline to glutamate for use as a carbon and nitrogen source and also function as a transcriptional repressor of the put operon. EcoCyc product frame: PUTA-MONOMER. EcoCyc synonyms: putC, poaA. Genomic coordinates: 1074920-1078882. EcoCyc protein note: PutA is a flavoprotein with mutually exclusive functions as a transcriptional repressor and membrane-associated enzyme. The switch between the two activities is due to conformational changes triggered by the redox state of FAD. In the presence of proline, PutA is associated with the cytoplasmic membrane and acts a bifunctional enzyme catalyzing both reactions of the PROUT-PWY-I pathway: the oxidation of proline by proline dehydrogenase and subsequent oxidation to glutamate by pyrroline-5-carboxylate (P5C) dehydrogenase. The kinetics of the coupled reaction is best described by substrate channeling. In the absence of proline, PutA is cytoplasmic and functions as a transcriptional repressor of the put regulon. The N-terminal 47 residues with a ribbon-helix-helix fold contain the dimerization domain and the specific DNA-binding activity of PutA . The Lys9 residue is essential for recognition of put promoter DNA . Crystal structures of this domain have been solved...

## Biological Role

Repressed by putA (protein.P09546), arcA (protein.P0A9Q1), yeiE (protein.P0ACR4), basR (protein.P30843). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09546|protein.P09546]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=putA; function=+
- `represses` <-- [[protein.P09546|protein.P09546]] `RegulonDB` `C` - regulator=PutA; target=putA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=putA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=putA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003424,ECOCYC:EG10801,GeneID:945600`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1074920-1078882:-; feature_type=gene
