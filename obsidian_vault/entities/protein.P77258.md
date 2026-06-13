---
entity_id: "protein.P77258"
entity_type: "protein"
name: "nemA"
source_database: "UniProt"
source_id: "P77258"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nemA ydhN b1650 JW1642"
---

# nemA

`protein.P77258`

## Static

- Type: `protein`
- Source: `UniProt:P77258`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the degradation of toxic compounds (PubMed:15184158, PubMed:17504490, PubMed:23506073, PubMed:23527133, PubMed:23536188, PubMed:9013822). Can use a variety of substrates, including the nitrate ester explosives glycerol trinitrate (GTN) and pentaerythritol tetranitrate (PETN), chromate and various electrophiles such as quinones (PubMed:15184158, PubMed:23506073, PubMed:23527133). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). Catalyzes the reduction of N-ethylmaleimide (NEM) to N-ethylsuccinimide (PubMed:23506073, PubMed:9013822). Together with NfsA and NfsB, can use the nitroaromatic explosive 2,4,6-trinitrotoluene (TNT) (PubMed:17504490). {ECO:0000269|PubMed:15184158, ECO:0000269|PubMed:17504490, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23527133, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:9013822}. N-ethylmaleimide reductase (NemA) is a member of the "old yellow enzyme" family of flavoproteins and catalyzes the reduction of N-ethylmaleimide (NEM) to N-ethylsuccinimide . NEM modifies the cysteine residues of cellular proteins and thus inhibits growth. NemA is probably involved in the degradation of toxic compounds and their reuse as a source of nitrogen...

## Biological Role

Catalyzes RXN0-5101 (reaction.ecocyc.RXN0-5101). Bound by FMN (molecule.C00061).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in the degradation of toxic compounds (PubMed:15184158, PubMed:17504490, PubMed:23506073, PubMed:23527133, PubMed:23536188, PubMed:9013822). Can use a variety of substrates, including the nitrate ester explosives glycerol trinitrate (GTN) and pentaerythritol tetranitrate (PETN), chromate and various electrophiles such as quinones (PubMed:15184158, PubMed:23506073, PubMed:23527133). Involved in resistance to hypochlorous acid (HOCl), which is the active component of household bleach and a powerful antimicrobial during the innate immune response (PubMed:23536188). Catalyzes the reduction of N-ethylmaleimide (NEM) to N-ethylsuccinimide (PubMed:23506073, PubMed:9013822). Together with NfsA and NfsB, can use the nitroaromatic explosive 2,4,6-trinitrotoluene (TNT) (PubMed:17504490). {ECO:0000269|PubMed:15184158, ECO:0000269|PubMed:17504490, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23527133, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:9013822}.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5101|reaction.ecocyc.RXN0-5101]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1650|gene.b1650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77258`
- `KEGG:ecj:JW1642;eco:b1650;ecoc:C3026_09470;`
- `GeneID:75171711;75204495;946164;`
- `GO:GO:0005829; GO:0006805; GO:0008748; GO:0010181; GO:0046857`
- `EC:1.3.1.-`

## Notes

N-ethylmaleimide reductase (NEM reductase) (EC 1.3.1.-) (N-ethylmaleimide reducing enzyme)
