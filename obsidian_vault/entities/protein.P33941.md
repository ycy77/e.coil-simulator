---
entity_id: "protein.P33941"
entity_type: "protein"
name: "yojI"
source_database: "UniProt"
source_id: "P33941"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yojI yojJ b2211 JW2199"
---

# yojI

`protein.P33941`

## Static

- Type: `protein`
- Source: `UniProt:P33941`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Mediates resistance to the antibacterial peptide microcin J25, when expressed from a multicopy vector. Functions as an efflux pump for microcin J25, with the help of the outer membrane channel TolC. {ECO:0000269|PubMed:15866933}. YojI is a member of the ABC superfamily of transporters . Sequence analysis suggests that yojI encodes an ABC-type exporter with six hydrophobic transmembrane segments and a single nucleotide-binding domain . Overexpression of yojI from a plasmid vector confers resistance to the peptide antibiotic, microcin J25; this resistance phenotype is abolished when a tolC null allele is present suggesting that YojI and TolC are components of an efflux system that can export microcin J25; YojI can substitute for McjD, the natural, plasmid encoded microcin J25 exporter . Expression of yojI is upregulated by guanosine 3',5'-bispyrophosphate (ppGpp) . The transcriptional regulator, Lrp, upregulates yojI expression . yojI is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Mediates resistance to the antibacterial peptide microcin J25, when expressed from a multicopy vector. Functions as an efflux pump for microcin J25, with the help of the outer membrane channel TolC. {ECO:0000269|PubMed:15866933}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2211|gene.b2211]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33941`
- `KEGG:ecj:JW2199;eco:b2211;ecoc:C3026_12355;`
- `GeneID:946705;`
- `GO:GO:0005524; GO:0015833; GO:0016020; GO:0016887; GO:0042626; GO:0042884; GO:0043190; GO:0046677; GO:0140359; GO:1904680`

## Notes

ABC transporter ATP-binding/permease protein YojI
