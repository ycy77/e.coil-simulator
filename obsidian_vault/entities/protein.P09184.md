---
entity_id: "protein.P09184"
entity_type: "protein"
name: "vsr"
source_database: "UniProt"
source_id: "P09184"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "vsr b1960 JW1943"
---

# vsr

`protein.P09184`

## Static

- Type: `protein`
- Source: `UniProt:P09184`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Deamination of 5-methylcytosine in DNA results in T/G mismatches. If unrepaired, these mismatches can lead to C-to-T transition mutations. The very short patch (VSP) repair process in E.coli counteracts the mutagenic process by repairing the mismatches in favor of the G-containing strand. This enzyme is an endonuclease that nicks double-stranded DNA within the sequence CT(AT)GN or NT(AT)GG next to the thymidine residue that is mismatched to 2'-deoxyguanosine. The incision is mismatch-dependent and strand-specific. {ECO:0000269|PubMed:10871403, ECO:0000269|PubMed:1944537}. Vsr is an endonuclease that specifically recognizes and exhibits strand-specific nicking at T:G DNA mismatches, which arise from spontaneous deamination at 5-methylcytosine, the product of Dcm (cytosine) methylation . Vsr activity counterbalances the mutagenesis associated with dcm activity . Vsr is an essential component of the very short patch (VSP) mismatch repair pathway, as is PolA , whereas MutL and MutS are involved but not essential . A minimal VSP pathway containing the purified components Vsr, PolA, DNA ligase I (LigA) and a plasmid substrate has been reconstituted in vitro . Vsr binding to MutL antagonizes MutL homodimerization and decreases interactions among MutL, MutS, and MutH . In vitro stimulation of Vsr requires MutS, MutL and ATP hydrolysis...

## Annotation

FUNCTION: Deamination of 5-methylcytosine in DNA results in T/G mismatches. If unrepaired, these mismatches can lead to C-to-T transition mutations. The very short patch (VSP) repair process in E.coli counteracts the mutagenic process by repairing the mismatches in favor of the G-containing strand. This enzyme is an endonuclease that nicks double-stranded DNA within the sequence CT(AT)GN or NT(AT)GG next to the thymidine residue that is mismatched to 2'-deoxyguanosine. The incision is mismatch-dependent and strand-specific. {ECO:0000269|PubMed:10871403, ECO:0000269|PubMed:1944537}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1960|gene.b1960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09184`
- `KEGG:ecj:JW1943;eco:b1960;ecoc:C3026_11085;`
- `GeneID:86946875;946476;`
- `GO:GO:0003677; GO:0006298; GO:0016787; GO:0043765; GO:0046872`
- `EC:3.1.-.-`

## Notes

DNA mismatch endonuclease Vsr (EC 3.1.-.-) (Type II nicking enzyme) (V.EcoKDcm) (Very short patch repair protein) (Vsr mismatch endonuclease)
