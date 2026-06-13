---
entity_id: "gene.b1212"
entity_type: "gene"
name: "prmC"
source_database: "NCBI RefSeq"
source_id: "gene-b1212"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1212"
  - "prmC"
---

# prmC

`gene.b1212`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1212`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prmC (gene.b1212) is a gene entity. It encodes prmC (protein.P0ACC1). Encoded protein function: FUNCTION: Methylates the class 1 translation termination release factors RF1/PrfA and RF2/PrfB on the glutamine residue of the universally conserved GGQ motif, i.e. on 'Gln-235' in RF1 and on 'Gln-252' in RF2. {ECO:0000269|PubMed:11805295, ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:16364916}. EcoCyc product frame: EG12424-MONOMER. EcoCyc synonyms: hemK. Genomic coordinates: 1266094-1266927. EcoCyc protein note: PrmC is a protein-(glutamine-N5) methyltransferase that methylates EG10761-MONOMER (RF1) and EG10762-MONOMER at their GGQ motifs . Methylation of these release factors increases termination efficiency . The PrmC/HemK family of proteins shows similarity to the gamma subfamily of S-adenosyl-methionine-dependent adenine-specific DNA methyltransferases . A crystal structure of PrmC is reported at 3.2 Å resolution . The C terminus contains a number of conserved residues surrounding the AdoHcy binding site . The N-terminal domain was suggested to determine methyltransferase substrate specificity and shows structural similarity to a number of protein-interacting domains . The crystal structure of a complex between RF1 and PrmC shows that the N-terminal domain interacts with both the GGQ motif and the central domain of RF1...

## Biological Role

Repressed by fnr (protein.P0A9E5), glaR (protein.P37338). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACC1|protein.P0ACC1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=prmC; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=prmC; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=prmC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004068,ECOCYC:EG12424,GeneID:945779`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1266094-1266927:+; feature_type=gene
