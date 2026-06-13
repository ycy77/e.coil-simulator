---
entity_id: "gene.b3412"
entity_type: "gene"
name: "bioH"
source_database: "NCBI RefSeq"
source_id: "gene-b3412"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3412"
  - "bioH"
---

# bioH

`gene.b3412`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3412`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioH (gene.b3412) is a gene entity. It encodes bioH (protein.P13001). Encoded protein function: FUNCTION: The physiological role of BioH is to remove the methyl group introduced by BioC when the pimeloyl moiety is complete. It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway through the hydrolysis of the ester bonds of pimeloyl-ACP esters. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. BioH shows a preference for short chain fatty acid esters (acyl chain length of up to 6 carbons) and short chain p-nitrophenyl esters. Also displays a weak thioesterase activity. Can form a complex with CoA, and may be involved in the condensation of CoA and pimelic acid into pimeloyl-CoA, a precursor in biotin biosynthesis.; FUNCTION: Catalyzes the hydrolysis of the methyl ester bond of dimethylbutyryl-S-methyl mercaptopropionate (DMB-S-MMP) to yield dimethylbutyryl mercaptopropionic acid (DMBS-MPA) during the biocatalytic conversion of simvastin acid from monacolin J acid. Can also use acyl carriers such as dimethylbutyryl-S-ethyl mercaptopropionate (DMB-S-EMP) and dimethylbutyryl-S-methyl thioglycolate (DMB-S-MTG) as the thioester substrates. EcoCyc product frame: EG10122-MONOMER. EcoCyc synonyms: bioB. Genomic coordinates: 3544074-3544844...

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13001|protein.P13001]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011136,ECOCYC:EG10122,GeneID:947916`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3544074-3544844:-; feature_type=gene
