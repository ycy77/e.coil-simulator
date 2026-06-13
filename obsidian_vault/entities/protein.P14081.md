---
entity_id: "protein.P14081"
entity_type: "protein"
name: "selB"
source_database: "UniProt"
source_id: "P14081"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "selB fdhA b3590 JW3563"
---

# selB

`protein.P14081`

## Static

- Type: `protein`
- Source: `UniProt:P14081`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Translation factor necessary for the incorporation of selenocysteine into proteins. It probably replaces EF-Tu for the insertion of selenocysteine directed by the UGA codon. SelB binds GTP and GDP. SelB is a specialized translation factor that takes the place of elongation factor EF-Tu for the insertion of selenocysteine into a peptide chain at the site of a UGA codon. Most UGA codons signal chain termination; a UGA codon that encodes selenocysteine insertion is distinguished from those that signal chain termination by a structured sequence, called SECIS (SElenoCysteine Insertion Sequence), immediately downstream of the UGA codon . SelB recognizes and binds to identical bases within the loop region in the SECIS hairpin structure of both fdhF and fdnG mRNAs, and thereby brings the charged modified-charged-selC-tRNA selenocysteyl-tRNASec (Sec-tRNASec) into the neighborhood of the UGA codon . Structures of several intermediates during delivery of Sec-tRNASec to the ribosome have been solved by single-particle cryo-electron microscopy, elucidating the dynamics of codon recognition and GTPase activation . SelB is found at a level of approximately 1100 copies per cell . The N-terminal domain of SelB shares extensive sequence similarity with EF-Tu and IF2 ; this domain binds specifically to Sec-tRNASec . Its structure was modeled based on that of Thermus thermophilus EF-Tu...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462). Component of SelB-L-selenocysteinyl-tRNAsec (complex.ecocyc.CPLX0-8053).

## Annotation

FUNCTION: Translation factor necessary for the incorporation of selenocysteine into proteins. It probably replaces EF-Tu for the insertion of selenocysteine directed by the UGA codon. SelB binds GTP and GDP.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8053|complex.ecocyc.CPLX0-8053]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3590|gene.b3590]] `RegulonDB` `C` - regulator=SelB-L-selenocysteinyl-tRNA<sup>sec</sup>; target=selB; function=-
- `represses` --> [[gene.b3591|gene.b3591]] `RegulonDB` `C` - regulator=SelB-L-selenocysteinyl-tRNA<sup>sec</sup>; target=selA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3590|gene.b3590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14081`
- `KEGG:ecj:JW3563;eco:b3590;ecoc:C3026_19465;`
- `GeneID:948103;`
- `GO:GO:0000049; GO:0001514; GO:0003746; GO:0003924; GO:0005525; GO:0005737; GO:0016259; GO:0019003; GO:0035368`

## Notes

Selenocysteine-specific elongation factor (SelB translation factor)
